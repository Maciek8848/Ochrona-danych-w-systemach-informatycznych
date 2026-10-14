
def szyfrujVigenere(dane, klucz):
    wynik = bytearray()
    for i in range(len(dane)):
        nowyBajt = (dane[i] + klucz[i % len(klucz)]) % 256
        wynik.append(nowyBajt)
    return bytes(wynik)

def deszyfrujVigenere(dane, klucz):
    wynik = bytearray()
    for i in range(len(dane)):
        nowyBajt = (dane[i] - klucz[i % len(klucz)]) % 256
        wynik.append(nowyBajt)
    return bytes(wynik)

klucz = b"ZAMEK"

file = open("tekst_pl.txt", "rb")
dane = file.read()
file.close()

zaszyfrowaneDane = szyfrujVigenere(dane, klucz)

szyfrFile = open("vigenere.bin", "wb")
szyfrFile.write(zaszyfrowaneDane)
szyfrFile.close()

odszyfrowaneDane = deszyfrujVigenere(zaszyfrowaneDane, klucz)
if dane == odszyfrowaneDane:
    print("Test pliku: Udany")
else:
    print("Test pliku: Nieudany")

danePuste = b""
dane0_255 = bytes([0, 255])

testPuste = deszyfrujVigenere(szyfrujVigenere(danePuste, klucz), klucz)
test0_255 = deszyfrujVigenere(szyfrujVigenere(dane0_255, klucz), klucz)

if testPuste == danePuste:
    print("Test pustych danych: Udany")
else:
    print("Test pustych danych: Nieudany")
if test0_255 == dane0_255:
    print("Test bajtow 0 i 255: Udany")
else:
    print("Test bajtow 0 i 255: Nieudany")


tekstJawny = b"BRAMABRAMABRAMA"
klucz1 = b"SZYFR"
klucz2 = b"KOD"

szyfr1 = szyfrujVigenere(tekstJawny, klucz1)
szyfr2 = szyfrujVigenere(tekstJawny, klucz2)

hexSzyfr = szyfr1.hex()
hexKod = szyfr2.hex()

print("Klucz SZYFR:", hexSzyfr[0:10], hexSzyfr[10:20], hexSzyfr[20:30])
print("Klucz KOD:  ", hexKod[0:10], hexKod[10:20], hexKod[20:30])