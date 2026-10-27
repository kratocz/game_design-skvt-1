"""Sestaví video úkolu: úvodní karta, záběry s vypálenými titulky, blok screenshotů blueprintů, závěrečný titulek.

Použití: python3 tools/build_video.py <segmenty.json> <výstup.mp4> [číslo_segmentu]

V JSON jsou adresáře záběrů a screenshotů relativně k JSON souboru (viz
docs/homeworks/02-plizeni/odevzdani/video-zalozni.json). S číslem segmentu se
vyrenderuje jen ten (na zkoušku titulků), bez spojení; úvodní karta (klíč
„intro“, nepovinný) je segment 1. Potřebuje ffmpeg-full
(brew, keg-only), výchozí ffmpeg z Homebrew nemá filtr subtitles.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

FF = "/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg"
FP = "/opt/homebrew/opt/ffmpeg-full/bin/ffprobe"
W, H, FPS = 1920, 1080, 30
INTRO_SEC, BP_SEC, OUTRO_SEC, TITLE_MAX = 5, 8, 9, 10.0

cfg_path = Path(sys.argv[1]).resolve()
cfg = json.loads(cfg_path.read_text())
out = Path(sys.argv[2]).resolve()
only = int(sys.argv[3]) if len(sys.argv) > 3 else None
work = Path(tempfile.gettempdir()) / f"build_video-{out.stem}"
work.mkdir(exist_ok=True)


def find(directory, name):
    # záznamy obrazovky z macOS mají název na disku v NFD a za „v“ pevnou mezeru (U+00A0),
    # v JSON bývá NFC s obyčejnou mezerou
    d = cfg_path.parent / directory

    def key(s):
        return unicodedata.normalize("NFC", s).replace("\xa0", " ")

    want = key(name)
    for f in os.listdir(d):
        if key(f) == want:
            return str(d / f)
    raise SystemExit(f"nenalezeno: {d / name}")

ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Bottom,Arial,46,&H00FFFFFF,&H00FFFFFF,&H80000000,&H80000000,0,0,0,0,100,100,0,0,3,14,0,2,220,220,60,1
Style: Top,Arial,40,&H00FFFFFF,&H00FFFFFF,&HB0000000,&HB0000000,0,0,0,0,100,100,0,0,3,12,0,8,120,120,24,1
Style: Center,Arial,50,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,260,260,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def ts(s):
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{sec:05.2f}"


def ass(path, text, style, start, end):
    # jednopísmenná předložka/spojka nesmí zůstat na konci řádku: pevná mezera \h
    text = re.sub(r"(?<=\s)([ksvzaiouKSVZAIOU]) ", r"\1\\h", text)
    fade = r"{\fad(300,300)}"
    path.write_text(ASS_HEAD + f"Dialogue: 0,{ts(start)},{ts(end)},{style},,0,0,0,,{fade}{text}\n", encoding="utf-8")


def dur(f):
    return float(subprocess.check_output([FP, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode())


# -nostdin u každého volání: ffmpeg jinak čte stdin a ve smyčce sní vstup dalších příkazů
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS),
       "-c:a", "aac", "-b:a", "96k", "-ar", "48000", "-ac", "2", "-shortest", "-movflags", "+faststart"]
SILENCE = ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]


def sub(a):
    return f"subtitles='{a}':fontsdir=/System/Library/Fonts/Supplemental"


segs = []
n = 0
if "intro" in cfg:
    n += 1
    a = work / f"{n:02d}.ass"
    ass(a, cfg["intro"], "Center", 0.3, INTRO_SEC - 0.3)
    segs.append((n, ["-f", "lavfi", "-t", str(INTRO_SEC), "-i", f"color=c=0x101010:s={W}x{H}:r={FPS}"] + SILENCE,
                 f"fade=t=out:st={INTRO_SEC - 0.5}:d=0.5,{sub(a)}", INTRO_SEC))

for s in cfg["shots"]:
    n += 1
    src = find(cfg["video_dir"], s["file"])
    d = dur(src)
    a = work / f"{n:02d}.ass"
    ass(a, s["t"], "Bottom", 0.4, min(d - 0.3, TITLE_MAX))
    # záznam je 2426x1422 (širší než 16:9 o pár řádků): oříznout na 16:9 a zmenšit
    vf = f"crop=iw:trunc(iw*9/16/2)*2,scale={W}:{H}:flags=lanczos,fps={FPS},fade=t=in:d=0.3,fade=t=out:st={d - 0.35:.2f}:d=0.3,{sub(a)}"
    segs.append((n, ["-i", src] + SILENCE, vf, None))

for b in cfg["blueprints"]:
    n += 1
    src = find(cfg["bp_dir"], b["file"])
    a = work / f"{n:02d}.ass"
    ass(a, b["t"], "Top", 0.2, BP_SEC - 0.2)
    vf = (f"scale={W - 80}:{H - 150}:force_original_aspect_ratio=decrease:flags=lanczos,"
          f"pad={W}:{H}:(ow-iw)/2:110+({H - 150}-ih)/2:color=0x1e1e1e,fps={FPS},format=yuv420p,"
          f"fade=t=in:d=0.3,fade=t=out:st={BP_SEC - 0.35}:d=0.3,{sub(a)}")
    segs.append((n, ["-loop", "1", "-t", str(BP_SEC), "-i", src] + SILENCE, vf, BP_SEC))

n += 1
a = work / f"{n:02d}.ass"
ass(a, cfg["outro"], "Center", 0.3, OUTRO_SEC - 0.3)
segs.append((n, ["-f", "lavfi", "-t", str(OUTRO_SEC), "-i", f"color=c=0x101010:s={W}x{H}:r={FPS}"] + SILENCE,
             f"fade=t=out:st={OUTRO_SEC - 0.5}:d=0.5,{sub(a)}", OUTRO_SEC))

files = []
for i, inputs, vf, t in segs:
    o = work / f"{i:02d}.mp4"
    files.append(o)
    if only is not None and i != only:
        continue
    cmd = [FF, "-nostdin", "-v", "error", "-y"] + inputs + ["-filter_complex", f"[0:v]{vf}[v]", "-map", "[v]", "-map", "1:a"]
    if t:
        cmd += ["-t", str(t)]
    subprocess.run(cmd + ENC + [str(o)], check=True)
    print("hotovo", o.name, flush=True)

if only is None:
    lst = work / "list.txt"
    lst.write_text("".join(f"file '{f}'\n" for f in files))
    subprocess.run([FF, "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
                    "-movflags", "+faststart", str(out)], check=True)
    print("výstup", out, dur(str(out)))
