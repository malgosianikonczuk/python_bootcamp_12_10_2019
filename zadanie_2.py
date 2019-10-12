"""
Zapytaj użytkownika o:
miasto_a, miasto_b, odleglosc miedzy nimi,
koszt paliwa, spalanie na 100 km.

Oblicz koszt podrozy pomiedzy tymi miastami
Wyswietl sformatowana odpowiedz

? python zadanie_2.py
Podaj nazwe miasta a: ...
Podaj nazwe miasta b: ...
Podaj odleglosc miedzy <miasto_a> a <miasto_b>:
Jaka jest cena paliwa?
Jakie jest spalanie?

Na trasie między <miasto a> a <miasto b> koszt podróży wynosi <cena_paliwa>
"""

miasto_a = input("Podaj nazwę miasta A: ").upper()
miasto_b = input("Podaj nazwę miasta B: ").upper()
odleglosc = int(input(f"Odległość między {miasto_a} a {miasto_b}: "))
koszt_paliwa = float(input("Koszt paliwa: "))
spalanie = float(input("Podaj średnie spalanie na 100 km: "))

koszt = (odleglosc / 100) * spalanie * koszt_paliwa
print(f"Koszt przejazdu między {miasto_a} a {miasto_b} wynosi {koszt}")

# Wyrażenia warunkowe

x = 90
y = 10
if x < y:
    print("Lewy dolny róg")
elif x==y:
    print("Centrum")
elif x > y:
    print("Prawy dolny róg")

