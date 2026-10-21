import math
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def oblicz_entropie(dane_bajt):
    dlugosc = len(dane_bajt)
    entropia = 0.0
    for i in range(256):
        licznosc = dane_bajt.count(bytes([i]))
        if licznosc > 0: 
            p_b = licznosc / dlugosc
            entropia -= p_b * math.log2(p_b)

    return entropia


with open("slaby_ecb.bin", "rb") as f:
    caly_kryptogram = f.read()

probka = caly_kryptogram[:4096]  
zbior_znakow = "abcdefghijklmnopqrstuvwxyz0123456789"
wyniki = []
for znak in zbior_znakow:
    klucz = (znak * 16).encode("utf-8")

    szyfr = AES.new(klucz, AES.MODE_ECB)
    odszyfrowanyKawalek = szyfr.decrypt(probka)


    wyniki.append((oblicz_entropie(odszyfrowanyKawalek), znak))

wyniki.sort()


for H, znak in wyniki[:5]:
    print(f"Znak klucza: '{znak}', Entropia H = {H:.4f}")
najlepszeH, najlepszy_znak = wyniki[0]
najlepszy_klucz = (najlepszy_znak * 16).encode("utf-8")

szyfrCaly = AES.new(najlepszy_klucz, AES.MODE_ECB)
odszyfrowanyCaly = unpad(szyfrCaly.decrypt(caly_kryptogram), AES.block_size)
tekst = odszyfrowanyCaly.decode("utf-8", errors="replace")
line = tekst.splitlines()[0]



print(f"Najlepsz znak klucza: '{najlepszy_znak}'")
print(f"Tekst: {line}")