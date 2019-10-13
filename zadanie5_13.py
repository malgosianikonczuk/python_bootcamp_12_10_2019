napis = input("Podaj napis: ")
samogłoski = [aeiouy]

licznik = 1
for litera in napis:
    if litera in samogłoski:
        licznik += 1

        print(f"znaleziono {} samogłosek")
