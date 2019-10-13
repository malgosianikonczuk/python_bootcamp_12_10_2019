#Tworzenie listy

lista = [] #pusta lista
lista1 = [1, 2, 3 ]
lista2 = [1, "2", "a", 3]
lista3 = [1, "2", ["a", 3]]

#funkcja tworząca listę: list

lista = list()

#lista ma swoje metody
print(dir(lista))
print(help(lista.append))
print("lista przed append:", lista)
lista.append(10)
print("lista po append:", lista)

print(lista.pop())
print("lista po pop:", lista)



[10, 20, 30, 40, 50] #wartości
#0,   1,  2,  3, 4   #indexy

lista = [10, 20, 30, 40, 50]
print(lista.index(50))

