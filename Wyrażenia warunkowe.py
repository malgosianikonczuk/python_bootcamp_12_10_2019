x = input("Podaj liczbę x: ")
y = input("Podaj_liczbę_y: ")

if x > y:
    print(f"{x} jest większe od {y}")
elif x < y:
    print(f"{x} jest mniejsze niż {y}")

# x = int(input("Podaj współrzędna x: "))
# y = int(input("Podaj współrzędna y: "))

x, y = 95, 95
# ctrl alt l - formatuje kod z godnie PyCharm (PEP8)
if x > 100 or y > 100 or x < 0 or y < 0:
    print("Jesteś poza planszą")
elif x > 90 and y > 90:
    print("Jesteś w PGR")
elif x > 90 and y < 10:
    print("Jesteś w PDR")
elif x < 10 and y > 90:
    print("Jesteś w PDR")
    