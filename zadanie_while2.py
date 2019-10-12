suma = 0
i = 0

while True:
    odp = input("Podaj liczbę lub wpisz 'k', aby zakończyć: ")
    if odp == "k":
        break
    odp = int(odp)
    suma = suma + odp
    i += 1




        print("Średnia wynosi: ", suma/i)
    else:
        print("Nie podano liczb")


# i = ilość powtórzeń, ile było powtórzeń, łączna suma podanych liczb