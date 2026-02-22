
# Frage den Namen des Benutzers ab und gib ihn in einem Begrüßungssatz aus.


namen_liste = []

zugabe_namen_liste = input("Hallo, wie heisst Du?: ")
namen_liste.append(zugabe_namen_liste)

print(namen_liste)
print("-" * 40)

# Frage zwei Zahlen ab und gib ihre Summe aus.

print("Gib mir 2 Zahlen aus und wir rechnen zusammen: ")
a = input()
print("-" * 40)

print("Gib mir noch eine Zahl:")
b = input()
print("-" * 40)

c = sum([int(i) for i in [a, b]])

print(c)
print("-" * 40)

#Erstelle zwei Listen mit jeweils drei beliebigen Namen
# (z. B. Freunde und Familie) und verbinde sie zu einer
# neuen Liste. Gib das Ergebnis aus.


zahlen_liste = []
print("Gib mir 4 Ganzzahlen: ")
zugabe_zahlen_liste = int(input("Die erste Zahl: "))
zahlen_liste.append(zugabe_zahlen_liste)
zugabe_zahlen_liste = int(input("Die zweite Zahl: "))
zahlen_liste.append(zugabe_zahlen_liste)
zugabe_zahlen_liste = int(input("Die dritte Zahl: "))
zahlen_liste.append(zugabe_zahlen_liste)
zugabe_zahlen_liste = int(input("Die vierte Zahl: "))
zahlen_liste.append(zugabe_zahlen_liste)


print(zahlen_liste)
print("-" * 40)


# Erstelle zwei Listen mit jeweils drei beliebigen Namen
# (z. B. Freunde und Familie) und verbinde sie zu einer neuen Liste.

list_1 = ["Sebastian, Patrick, Till"]
list_2 = ["Erwin, Tobias, Marcel"]

print(list_1)
print("-" * 40)

print(list_2)
print("-" * 40)

list_1.extend(list_2)
print(list_1)
print("-" * 40)


#Erstelle eine Liste mit fünf Lieblingsspeisen.
#Gib das erste, das mittlere und das letzte Element aus.

lieblingsessen = ("Pad_Thai", "Spaghetti_Carbonara", "Schokolade", "Pudding", "Gummiviecher")

print(lieblingsessen [0], lieblingsessen [2], lieblingsessen [4] )
print("-" * 40)


#Erstelle eine Liste mit vier Zahlen deiner Wahl.
#Gib folgende Informationen aus:
#•	Länge der Liste
#•	Summe aller Zahlen
#•	Größte und kleinste Zahl
#Tipp:
#→ len(), sum(), max(), min().

#zahlen_liste = [5, 6, 80, 50]

print(len(zahlen_liste))
print(sum(zahlen_liste))
print(max(zahlen_liste))
print(min(zahlen_liste))
print("-" * 40)

