import hashlib


def h24(dane):
    return hashlib.sha256(dane).hexdigest()[:6]


def wariant(wiersze, v):
    wynik = b""
    for i, w in enumerate(wiersze):
        if (v >> i) & 1:
            w = w[:-1] + b" " + b"\n"
        wynik += w
    return wynik


with open("oryginal.txt", "rb") as f:
    wiersze_o = f.read().splitlines(keepends=True)
with open("zmieniony.txt", "rb") as f:
    wiersze_z = f.read().splitlines(keepends=True)

slownik = {}
for v in range(8192):
    slownik[h24(wariant(wiersze_o, v))] = v

h_oryg = h24(wariant(wiersze_o, 0))
para = None
licznik = 0
for v in range(8192):
    h = h24(wariant(wiersze_z, v))
    if h == h_oryg:
        licznik += 1
    if para is None and h in slownik:
        para = (slownik[h], v, h)

print("Para (v_oryginał, v_zmieniony), h24:", para)
print("Liczba wariantów zmienionego z h24 równym wariantowi 0 oryginału:", licznik)