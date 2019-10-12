import random
DEBUG = True
#losuję pozycję skarbu:
skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

#losuję pozycję gracza:
gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)

#minimalna liczba ruchów po wylosowaniu
min_l_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
print("Położenie gracza:", gracz_x, gracz_y)
print("Położenie skarbu:", skarb_x, skarb_y)

if DEBUG:
    print("Położenie gracza:", gracz_x, gracz_y)
    print("Położenie skarbu:", skarb_x, skarb_y)



while True:
    min_l_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    ruch = input("Wykonaj ruch w(góra) a(lewo) s(dół) d(prawo)")
    if ruch == "w":
        gracz_y += 1
    if ruch == "s":
        gracz_y += -1
    if ruch == "a":
        gracz_x += 1
    if ruch == "d":
        gracz_x += -1

    min_l_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

    if sk
