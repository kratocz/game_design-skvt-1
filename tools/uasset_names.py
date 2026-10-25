import re
import struct
import sys

# Vypíše řetězce s délkovým prefixem (FString: int32 délka vč. nuly, znaky, \0),
# jak je UE ukládá do tabulky názvů balíčku, v pořadí výskytu.
for path in sys.argv[1:]:
    data = open(path, "rb").read()
    print("==", path.rsplit("/", 1)[-1])
    i, out = 0, []
    while i < len(data) - 5:
        (n,) = struct.unpack_from("<i", data, i)
        if 2 <= n <= 80 and i + 4 + n <= len(data):
            s = data[i + 4:i + 4 + n]
            if s[-1] == 0 and re.fullmatch(rb"[A-Za-z0-9_/.:\- ]+", s[:-1]):
                out.append((i, s[:-1].decode()))
                i += 4 + n
                continue
        i += 1
    for off, s in out:
        print(f"{off:6d} {s}")
