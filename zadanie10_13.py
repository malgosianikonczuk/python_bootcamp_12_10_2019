napis = "kryptorurki robaczne ramblowane poprzecznie"
liczniki = {}
for znak in napis.lower():
        liczniki[znak] = liczniki.get(znak, 0) + 1
print(liczniki)


#druga opcja
from collections import defaultdict