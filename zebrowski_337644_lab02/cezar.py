with open("cezar.bin", "rb") as file:
    dane = file.read()

wyniki = []


for key in range(256):
    count = 0
    for c in dane:
        p = (c - key) % 256
        if (p >= 32 and p <= 126) or p == 9 or p == 10 or p == 13:
            count += 1
    wynik = count
    wyniki.append(wynik)

Top5wyniki = []
Top5klucz = []

for x in range(5):
    maxWynik = -1
    maxklucz = 0
    
    for i in range(256):
        if wyniki[i] > maxWynik:
            maxWynik = wyniki[i]
            maxklucz = i
            
    Top5wyniki.append(maxWynik)
    Top5klucz.append(maxklucz)
    
    wyniki[maxklucz] = -1

print("Najlepsze wyniki: ", Top5wyniki)
print("Klucze najlebszych wynikow: ", Top5klucz)

for i in range(5):
    key = Top5klucz[i]
    wynik = Top5wyniki[i]
    
    poczatek = ""
    for j in dane[0:20]:
        p = (j - key) % 256
        poczatek += chr(p)
            
    print("Klucz:", key, " Wynik:", wynik, " Tresc:", poczatek)

file = open("cezar.txt", "w")
for i in dane:
    p = (i - Top5klucz[1]) % 256
    file.write(chr(p))
file.close()