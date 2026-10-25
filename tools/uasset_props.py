import re
import struct
import sys

# Najde tabulku názvů balíčku (souvislý řetěz FString + 4 B hash) a pro zadané
# názvy vlastností vypíše hodnoty float/bool/double serializované za jejich tagem.
# Heuristika pro tagy UE 5.4+ (FPropertyTypeName); ověřuje se na známých hodnotách.

def strings(data):
    out, i = [], 0
    while i < len(data) - 5:
        (n,) = struct.unpack_from("<i", data, i)
        if 2 <= n <= 200 and i + 4 + n <= len(data):
            s = data[i + 4:i + 4 + n]
            if s[-1] == 0 and re.fullmatch(rb"[ -~]+", s[:-1]):
                out.append((i, n, s[:-1].decode()))
                i += 4 + n
                continue
        i += 1
    return out

def name_map(data):
    ss = strings(data)
    best = []
    for k in range(len(ss)):
        chain = [ss[k]]
        for nxt in ss[k + 1:]:
            off, n, _ = chain[-1]
            if nxt[0] == off + 4 + n + 4:
                chain.append(nxt)
            elif nxt[0] > off + 4 + n + 4:
                break
        if len(chain) > len(best):
            best = chain
    return [s for _, _, s in best]

path, wanted = sys.argv[1], sys.argv[2:]
data = open(path, "rb").read()
names = name_map(data)
idx = {s: i for i, s in enumerate(names)}
print("names:", len(names))
for w in wanted:
    if w not in idx:
        print(f"{w}: (není v tabulce názvů)")
        continue
    key = struct.pack("<ii", idx[w], 0)
    for m in re.finditer(re.escape(key), data):
        p = m.end()
        (t,) = struct.unpack_from("<i", data, p)
        tname = names[t] if 0 <= t < len(names) else "?"
        raw = data[p:p + 32].hex(" ")
        val = ""
        if tname in ("FloatProperty", "DoubleProperty", "IntProperty"):
            # FName typu (8 B) + počet vnořených (4 B) + Size (4 B) + Flags (1 B) + hodnota
            q = p + 8 + 4
            (size,) = struct.unpack_from("<i", data, q)
            v = data[q + 5:q + 5 + size]
            if tname == "FloatProperty" and size == 4:
                val = struct.unpack("<f", v)[0]
            elif tname == "DoubleProperty" and size == 8:
                val = struct.unpack("<d", v)[0]
            elif tname == "IntProperty" and size == 4:
                val = struct.unpack("<i", v)[0]
        print(f"{w} @{m.start()} type={tname} value={val}  raw={raw}")
