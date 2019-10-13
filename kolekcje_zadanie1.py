lista = []

while len(lista) < 10:
    odp = input("Podaj dowolną liczbę lub naciśnij k aby przerwać:")
    if odp == "k":
        break
    print(len(lista))
    lista.append(int(odp))
srednia =sum(lista) / len(lista)
print(f"Średnia wynosi: {srednia}, min: {min(lista)}, max: {max(lista)}")

