import math
import time

def rc4(dane, klucz):
    s = list(range(256))
    j = 0
    dlugoscKlucza = len(klucz)
    
    for i in range(256):
        j = (j + s[i] + klucz[i % dlugoscKlucza]) % 256
        s[i], s[j] = s[j], s[i]
        
    wynik = bytearray()
    i = 0
    j = 0
    for b in dane:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % 256]
        wynik.append(b ^ k)
        
    return bytes(wynik)

def policzEntropie(dane):
    if len(dane) == 0:
        return 0
        
    wystapienia = [0] * 256
    for b in dane:
        wystapienia[b] += 1
        
    entropia = 0
    dlugosc = len(dane)
    for zliczenie in wystapienia:
        if zliczenie > 0:
            prawdopodobienstwo = zliczenie / dlugosc
            entropia -= prawdopodobienstwo * math.log2(prawdopodobienstwo)
            
    return entropia

daneTestowe = b"TEST3235i34u95"
kluczTestowy = b"abc"
if rc4(rc4(daneTestowe, kluczTestowy), kluczTestowy) == daneTestowe:
    print("Test szyfrowania RC4: Zgodny")
else:
    print("Test szyfrowania RC4: Niezgodny")

print("Szukanie klucza")
startCzas = time.time()

plikWejsciowy = open("rc4.bin", "rb")
danePliku = plikWejsciowy.read()
plikWejsciowy.close()

daneProbka = danePliku[:512]

alfabet = b"abcdefghijklmnopqrstuvwxyz"
wynikiKlucze = []
wynikiEntropia = []
liczbaProb = 0

for key1 in alfabet:
    for key2 in alfabet:
        for key3 in alfabet:
            liczbaProb += 1
            klucz = bytes([key1, key2, key3])
            
            odszyfrowane = rc4(daneProbka, klucz)
            entropia = policzEntropie(odszyfrowane)
            
            wynikiKlucze.append(klucz)
            wynikiEntropia.append(entropia)

top5Klucze = []
top5Entropia = []

for x in range(5):
    bestScore = 10000
    bestKluczIndeks = 0
    
    for i in range(len(wynikiEntropia)):
        if wynikiEntropia[i] < bestScore:
            bestScore = wynikiEntropia[i]
            bestKluczIndeks = i
            
    top5Entropia.append(bestScore)
    top5Klucze.append(wynikiKlucze[bestKluczIndeks])
    
    wynikiEntropia[bestKluczIndeks] = 10000

koniecCzas = time.time()
czasSzukania = koniecCzas - startCzas

for i in range(5):
    print("Miejsce", i+1, "Klucz:", top5Klucze[i].decode(), "Entropia:", top5Entropia[i])

print("\nLiczba prob:", liczbaProb)
print("Czas:", czasSzukania, "sekund")


najlepszyKlucz = top5Klucze[0]
print("Najlepszy klucz:", najlepszyKlucz.decode())

calyOdszyfrowanyTekst = rc4(danePliku, najlepszyKlucz)

plikWyjsciowy = open("rc4.txt", "wb")
plikWyjsciowy.write(calyOdszyfrowanyTekst)
plikWyjsciowy.close()


ponowneSzyfrowanie = rc4(calyOdszyfrowanyTekst, najlepszyKlucz)
if ponowneSzyfrowanie == danePliku:
    print("Test ponownego szyfrowania: Zgodny")
else:
    print("Test ponownego szyfrowania: Niezgodny")


entropiaKryptogramu = policzEntropie(danePliku)
entropiaCalyTekst = policzEntropie(calyOdszyfrowanyTekst)


print("Entropia zaszfyrowanego pliku: ", entropiaKryptogramu)
print("Entropia odszyfrowanego pliku: ", entropiaCalyTekst)