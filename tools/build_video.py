"""Sestaví video úkolu: úvodní karta, záběry s vypálenými titulky, blok screenshotů blueprintů, závěrečný titulek.

Použití: python3 tools/build_video.py <segmenty.json> <výstup.mp4> [číslo_segmentu]

V JSON jsou adresáře záběrů a screenshotů relativně k JSON souboru (viz
docs/homeworks/02-plizeni/odevzdani/video-zalozni.json). S číslem segmentu se
vyrenderuje jen ten (na zkoušku titulků), bez spojení; úvodní karta (klíč
„intro“, nepovinný) je segment 1. Záběr může mít ořez „ss“/„to“ v sekundách,
„hold“ (podržení posledního snímku v sekundách, když se do záběru nevejde hlas)
a prázdné „t“ (pokračování záběru se stejným titulkem); „cards“ jsou karty
{"t", "sec"} za záběry, „outro_sec“ délka závěrečného titulku. Hlas: „voice_dir“
a soubory v „voice“ u záběru či karty, „intro_voice“, „outro_voice“; hlas začíná
0,4 s po začátku segmentu, karty se podle něj prodlouží, záběr se nemění (hlas
smí přesáhnout do dalšího segmentu, ne do dalšího hlasu). Potřebuje ffmpeg-full
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

from PIL import ImageFont

FF = "/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg"
FP = "/opt/homebrew/opt/ffmpeg-full/bin/ffprobe"
FPS = 30
H = int(os.environ.get("VIDEO_H", 1080))  # výška výstupu, např. VIDEO_H=1440 pro verzi na YouTube
W = H * 16 // 9
K = H / 1080  # okraje kolem screenshotů jsou navržené pro 1080p; titulky (ASS) se škálují samy podle PlayRes
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
Style: Bottom,Arial,46,&H00FFFFFF,&H00FFFFFF,&H60000000,&H60000000,0,0,0,0,100,100,0,0,4,0,14,2,220,220,60,1
Style: Top,Arial,40,&H00FFFFFF,&H00FFFFFF,&HB0000000,&HB0000000,0,0,0,0,100,100,0,0,3,12,0,8,120,120,24,1
Style: Center,Arial,50,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,260,260,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def ts(s):
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{sec:05.2f}"


ARIAL = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)  # ASS 46 ≈ em 40 (libass: výška = ascent + descent)
LINE_MAX = 1440  # 1920 bez okrajů 2 × 220 a podkladu
SPACER = r"\N{\fs11}\h\N{\fs46}"  # prázdný řádek o čtvrtinu výšky: ASS řádkování nemá


def wrap(text):
    # jednopísmenná předložka/spojka nesmí zůstat na konci řádku: slepit s dalším slovem
    words = []
    for w in text.split(" "):
        if words and re.fullmatch(r"[ksvzaiouKSVZAIOU]", words[-1].split("\\h")[-1]) and not words[-1].endswith((".", ",")):
            words[-1] += "\\h" + w
        else:
            words.append(w)

    def width(s):
        return ARIAL.getlength(s.replace("\\h", " "))

    if width(" ".join(words)) <= LINE_MAX:
        return " ".join(words)
    # dva řádky: co nejvyrovnanější, zlom raději za interpunkcí (bonus 150 px)
    best = None
    for k in range(1, len(words)):
        a, b = " ".join(words[:k]), " ".join(words[k:])
        if max(width(a), width(b)) > LINE_MAX:
            continue
        cost = max(width(a), width(b)) - (150 if words[k - 1][-1] in ".,;:" else 0)
        if best is None or cost < best[0]:
            best = (cost, a, b)
    if best is None:
        raise SystemExit(f"titulek se nevejde na dva řádky: {text}")
    return best[1] + SPACER + best[2]


def ass(path, text, style, start, end):
    if style == "Bottom":
        text = wrap(text)
    else:
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
GAME_DB = 8  # zvuk hry ze záznamu; pod hlasem se ztlumí ještě kompresorem (ducking)


def has_audio(f):
    return bool(subprocess.check_output([FP, "-v", "error", "-select_streams", "a", "-show_entries", "stream=index",
                                         "-of", "csv=p=0", f], stdin=subprocess.DEVNULL).strip())


def sub(a):
    return f"subtitles='{a}':fontsdir=/System/Library/Fonts/Supplemental"


VOICE_LEAD = 0.4  # hlas začíná 0,4 s po začátku segmentu
voices = []  # (číslo segmentu, soubor, délka)


def voice(name):
    # ticho na krajích pryč (zůstane 0,1 s), hučení pod 80 Hz pryč, hlasitost na −16 LUFS (web)
    if not name:
        return 0
    o = work / f"voice-{Path(name).stem}.wav"
    af = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.1,areverse,"
          "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.1,areverse,"
          "highpass=f=80,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000")
    subprocess.run([FF, "-nostdin", "-v", "error", "-y", "-i", find(cfg["voice_dir"], name), "-af", af, "-ac", "1", str(o)],
                   check=True)
    v = dur(str(o))
    voices.append((n, o, v))
    return v


def card(text, sec, voice_name, fade_in=True):
    # karta na tmavém pozadí; s hlasem trvá aspoň do jeho konce + 0,8 s
    sec = max(sec, VOICE_LEAD + voice(voice_name) + 0.8)
    a = work / f"{n:02d}.ass"
    ass(a, text, "Center", 0.3, sec - 0.3)
    vf = ("fade=t=in:d=0.3," if fade_in else "") + f"fade=t=out:st={sec - 0.5}:d=0.5,{sub(a)}"
    segs.append((n, ["-f", "lavfi", "-t", str(sec), "-i", f"color=c=0x101010:s={W}x{H}:r={FPS}"] + SILENCE, vf, sec, None))


segs = []  # (číslo, vstupy, filtr obrazu, délka, filtr zvuku záznamu nebo None)
game_audio = False
n = 0
if "intro" in cfg:
    n += 1
    card(cfg["intro"], INTRO_SEC, cfg.get("intro_voice"), fade_in=False)

for s in cfg["shots"]:
    n += 1
    src = find(cfg["video_dir"], s["file"])
    ss = s.get("ss", 0)
    src_d = s.get("to", dur(src)) - ss
    hold = s.get("hold", 0)  # záběr na konci podržet na posledním snímku (aby se do něj vešel hlas)
    d = src_d + hold
    v = voice(s.get("voice"))
    if VOICE_LEAD + v > d:
        print(f"segment {n}: hlas přesahuje záběr o {VOICE_LEAD + v - d:.1f} s do dalšího", flush=True)
    # záznam bývá širší než 16:9 (2426x1422, z OBS 2560x1600): oříznout na 16:9 a zmenšit
    vf = (f"crop=iw:trunc(iw*9/16/2)*2,scale={W}:{H}:flags=lanczos,fps={FPS},"
          + (f"tpad=stop_mode=clone:stop_duration={hold}," if hold else "")
          + f"fade=t=in:d=0.3,fade=t=out:st={d - 0.35:.2f}:d=0.3")
    if s["t"]:
        a = work / f"{n:02d}.ass"
        ass(a, s["t"], "Bottom", 0.4, min(d - 0.3, max(TITLE_MAX, VOICE_LEAD + v + 0.3)))
        vf += f",{sub(a)}"
    # záznam se zvukem hry: zvuk ze záznamu s prolínáním jako obraz, jinak ticho
    af = (f"aformat=sample_rates=48000:channel_layouts=stereo,volume={GAME_DB}dB,alimiter=limit=0.7:level=false,"
          + (f"apad=pad_dur={hold}," if hold else "")
          + f"afade=t=in:d=0.3,afade=t=out:st={src_d - 0.35:.2f}:d=0.3") if has_audio(src) else None
    game_audio = game_audio or af is not None
    segs.append((n, ["-ss", str(ss), "-t", f"{src_d:.3f}", "-i", src] + SILENCE, vf, d, af))

for c in cfg.get("cards", []):
    n += 1
    card(c["t"], c["sec"], c.get("voice"))

for b in cfg["blueprints"]:
    n += 1
    src = find(cfg["bp_dir"], b["file"])
    a = work / f"{n:02d}.ass"
    ass(a, b["t"], "Top", 0.2, BP_SEC - 0.2)
    bw, bh, top = W - round(80 * K), H - round(150 * K), round(110 * K)
    vf = (f"scale={bw}:{bh}:force_original_aspect_ratio=decrease:flags=lanczos,"
          f"pad={W}:{H}:(ow-iw)/2:{top}+({bh}-ih)/2:color=0x1e1e1e,fps={FPS},format=yuv420p,"
          f"fade=t=in:d=0.3,fade=t=out:st={BP_SEC - 0.35}:d=0.3,{sub(a)}")
    segs.append((n, ["-loop", "1", "-t", str(BP_SEC), "-i", src] + SILENCE, vf, BP_SEC, None))

n += 1
card(cfg["outro"], cfg.get("outro_sec", OUTRO_SEC), cfg.get("outro_voice"), fade_in=False)

files = []
for i, inputs, vf, t, af in segs:
    o = work / f"{i:02d}.mp4"
    files.append(o)
    if only is not None and i != only:
        continue
    fc = f"[0:v]{vf}[v]" + (f";[0:a]{af}[a]" if af else "")
    cmd = [FF, "-nostdin", "-v", "error", "-y"] + inputs + ["-filter_complex", fc, "-map", "[v]",
                                                            "-map", "[a]" if af else "1:a"]
    if t:
        cmd += ["-t", str(t)]
    subprocess.run(cmd + ENC + [str(o)], check=True)
    print("hotovo", o.name, flush=True)

if only is None:
    lst = work / "list.txt"
    lst.write_text("".join(f"file '{f}'\n" for f in files))
    joined = work / "joined.mp4" if voices else out
    subprocess.run([FF, "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
                    "-movflags", "+faststart", str(joined)], check=True)
    if voices:
        # hlas na časové ose: začátek segmentu podle skutečné délky vyrenderovaných souborů
        starts, acc = {}, 0.0
        for (i, *_), f in zip(segs, files):
            starts[i] = acc
            acc += dur(str(f))
        placed = sorted((starts[i] + VOICE_LEAD, o, v) for i, o, v in voices)
        for (t0, o0, v0), (t1, o1, _) in zip(placed, placed[1:]):
            if t0 + v0 > t1:
                raise SystemExit(f"hlas {o0.name} zasahuje do {o1.name} o {t0 + v0 - t1:.1f} s")
        cmd = [FF, "-nostdin", "-v", "error", "-y", "-i", str(joined)]
        fc = []
        for k, (t0, o, _) in enumerate(placed, 1):
            cmd += ["-i", str(o)]
            fc.append(f"[{k}:a]adelay=delays={int(t0 * 1000)}:all=1[a{k}]")
        mix = "".join(f"[a{k}]" for k in range(1, len(placed) + 1))
        if game_audio:
            # zvuk hry se pod hlasem ztlumí (sidechain kompresor řízený hlasem) a pak se s hlasem smíchá
            fc.append(f"{mix}amix=inputs={len(placed)}:normalize=0:duration=longest,apad,"
                      f"aformat=sample_rates=48000:channel_layouts=stereo,asplit[vk][vm]")
            fc.append("[0:a]aformat=sample_rates=48000:channel_layouts=stereo[g];"
                      "[g][vk]sidechaincompress=threshold=0.02:ratio=6:attack=40:release=500[gd];"
                      "[gd][vm]amix=inputs=2:normalize=0:duration=first[a]")
        else:
            fc.append(f"{mix}amix=inputs={len(placed)}:normalize=0:duration=longest,apad,aformat=channel_layouts=stereo[a]")
        subprocess.run(cmd + ["-filter_complex", ";".join(fc), "-map", "0:v", "-map", "[a]", "-c:v", "copy",
                              "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-t", f"{acc:.3f}", "-movflags", "+faststart",
                              str(out)], check=True)
    print("výstup", out, dur(str(out)))
