Raport z laboratorium 2


Zadanie 1
Czym zaszyfrowana wiadomość szyfrem cezara jest dłuższa, tym prościej ją odszyfrować.

Przesunięcie: 233
Klucz ten ma najwyższy wynik (2859), a po jego użyciu początek tekstu jest czytelny.
Szyfr Cezara nie zmienia częstotliwość występowania poszczególnych liter, dlatego wynik entropii dla wszystkich 256 kluczy jest identyczny.



Zadanie 2
Słowo BRAMA i klucz SZYFR mają po 5 bajtów, więc tekst za każdym razem szyfruje się tym samym fragmentem klucza co daje identyczne bloki, a klucz KOD ma 3 bajty, co powoduje przesunięcie i brak powtórzeń.
Widoczne powtórzenia fragmentów pozwalają atakującemu łatwo odgadnąć długość użytego klucza.



Zadanie 3
Klucz: tat
Miejsce 1 Klucz: tat Entropia: 4.391044183197801
Miejsce 2 Klucz: neg Entropia: 7.430376480028585
Miejsce 3 Klucz: mcn Entropia: 7.451232162876939
Miejsce 4 Klucz: oxo Entropia: 7.453573837340277
Miejsce 5 Klucz: tnx Entropia: 7.459152626797808
Liczba prob: 17576
Czas: 2.9552440643310547 sekund
Entropia zaszfyrowanego pliku:  7.927093966754655
Entropia odszyfrowanego pliku:  4.325866591933658

RC4 jest oparty na bramce XOR. Odszyfrowanie dowolnym kluczem, a następnie ponowne zaszyfrowanie tym samym kluczem odwraca operację i zwraca te same dane co na początku.
Ale może zawieść, gdy tekst źródłowy jest plikiem skompresowanym (ma wysoką entropię) albo błędny klucz da same zera.