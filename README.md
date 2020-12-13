# Lista 10 - Języki programowania wysokiego poziomu

**N-tki i Słowniki**

Zadania:

(1) N-tki (tuples) są stałymi listami. W ich definicji stosujemy nawiasy okrągłe zamiast kwadratowych. Np.:
ntka=(1,’alfa’,5,3.14) określa 4 elementową n-tkę. Dostęp do poszczególnych
elementów uzyskujemy tak jak dla list poprzez:
print(ntka[0], ntka[3], nttka[-2]) co wyświetli pierwszy, czwarty i drugi od
końca element n-tki ntka.
Można przechodzić pomiędzy ntkami a listami i na odwrót ta pomocą l=list(t)
oraz t=tuple(l). Zdefiniuj ntki t1 i t2 z kilkoma elementami. Przetestuj na
nich operacje i funkcje: +, *2, len, max
Spróbuj zmienić pojedynczy element ntki t1. Jak się nie da, zrób to przechodząc przez listę l, usuwając t1 (polecenie del) i przepisując l do nowego
t1. Sprawdź za pomocą print.

(2) Słowniki przypominają listy, ale zamiast indeksowania liczbami naturalnymi 0,1,2... można indeksować dowolnymi stałymi elementami w pythonie
(czyli liczbami, łańcuchami, n-tkami). Przykładowa składnia:
sl={’Imię’: Anna, ’Wiek’:30, 5:’Costam’, (6,2):32}
Takie sl ma 4 indeksy (’Imię’, ’Wiek’, 5, (6,2)) za pomocą których możemy
otrzymać zawartości: sl[’Imię’], sl[5] itd.
Nowe pole możemy dodawać przez:
sl[’dodatki’]=’Costam’
Przetestuj za pomocą print: sl.keys(), sl.values() i sl.
Aby usunąć element sl: del sl[’Wiek’]
Stwórz 2 listy tej samej długości l1 i l2 bez powtarzających się elementów
w l1. Za pomocą pętli for stwórz słownik dict (przed pętlą pusty dict={})
którego indeksy są w l1 a wartości w l2. Sprawdź za pomocą print.

(3) Napisz funkcję bezpowt(sl) która pobiera jako parametr słownik, sprawdza czy wśród jego wartości jakieś elementy są takie same czy nie i zwraca
1 (jeśli nie ma powtórzeń) lub 0 (jeśli są). Przetestuj na dwóch słownikach, jednym z powtórzeniami, a drugim bez. Wsk.: może być pomocna
lista l=list(sl.values())

(4) Stosując funkcję z (3) napisz funkcję odwr(sl) która ma sprawdzić czy
nie ma powtórzeń wśród wartości sl i jeśli ich nie ma tworzy i zwraca słownik
sl2 w którym indeksy i wartości są zamienione. Jeśli są powtórzenia funkcja
wyświetla komunikat o błędzie.
Przetestuj tworząć kilkuelementowy słownik polsko-angielski. Funkcja powinna stworzyć z niego słownik angielsko-polski.

(5) Stwórz krótki słownik sl z indeksami i wartościami łańcuchy znaków, np.
taki jak w (4). Następnie wygeneruj plik zawierający klucz:wartość;klucz:wartość;itd..
Np. jeśli sl[’kot’]=’cat’, to plik może się zaczynać od: kot:cat;
Sprawdź czy plik został poprawnie stworzony.

(6) Korzystając z pliku wygenerowanego w (5) odtwórz słownik sl
