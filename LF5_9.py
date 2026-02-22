
# anstatt statischer Zuweisung von Werten wollen wir nun eine Nutzerabfrage vornehmen
print("Bitte geben Sie eine Zahl ein:")
wert1 = input() #Die Funktion input() fragt nun eine Eingabe des Nutzers aus der CMD ab
print(wert1)

wert2 = input("Bitte geben Sie eine zweite Zahl ein: ") #Die Aufforderung kann auch direkt in der input Funktion stehen
print(wert2)

# Eingaben sind standardmäßig Strings, also Zeichenketten
# diese müssen erst noch umgewandelt werden, wenn wir Zahlen und Mathe wollen.
# print(wert1/wert2) Ohne Anpassung gibt eine Teilung wert1/wert2 einen TypeError

# Anpassung von der Nutzereingabe
wert_int_1 = int(wert1)         #int() konvertiert den Wert der Variable "wert1" in eine Integer
wert_int_2 = int(wert2)         #float89, bool(), str() sind weitere Konvertierungsmöglichkeiten

print(f"{wert_int_1/wert_int_2:.2f}")
print(round(wert_int_1/wert_int_2,26))

from _pydecimal import Decimal

# kleiner Einschub
# Python hat wie alle Programmiersprachen nur eine endliche Maschiengenauigket
# bei einigen Gleitkommazahlen werden die Ergebnisse ab einem Punkt ungenau

# Beispiel für Machienengnauigkeit
a=0.1
b=0.2
c=0.3
a = Decimal('0.1')
b = Decimal('0.2')
c = Decimal('0.3')
print(a+b)
print(c)
print(a+b == c)

# Bislang haben wir jeder Variable genau einen Wert zugewiesen
# a=0.1 ist genau der Wert 0.1
# Es gibt Möglichkeiten, mehrere Daten hinter einer Variable zu speichern.
# Dies sind dann Datensammlungen (Data Collections)

# Für uns reicht erstmal die Liste.
# Eine Liste wird mit [] dargestellt

leere_liste = []    #ist genau die Bezeichnung, eine Liste, die noch keinen Inhalt hat
int_list = [84, 65, 37, 89, 645, 798, 65, 3, 97, 864, 58, 653]
#Liste mit Integern
mixed_list = ["Gerold", 52, 1.76, "∞", True]
#gemischte Liste, Listen können von sich aus alle Datentypen gleichzeitig halten
print(int_list)
print(int_list[4])
#Listen sind durchnummeriert und beginnen bei 0

print(leere_liste)

# Um neue Einträge zu erhalten, kann die Operation .append() verwendet werden

zugabe_leere_liste = input("Eingabe in die leere Liste: ")
leere_liste.append(zugabe_leere_liste)
leere_liste.append(input("Eingabe in die leere Liste: "))

# klappt auch mit Input in der Operation
# leere_liste ist der Bezeichner der Liste
# dahinter .append() ist die Operation, die auf der Liste ausgeführt werden

print(leere_liste)
leere_liste.pop(0)

# mit der Operation .pop() wird entweder das letzte Element oder der angegebene Index gelöscht

print(leere_liste)
print(mixed_list)
mixed_list.pop()
print(mixed_list)

# Listen können auch sortiert werden, die geschieht mithilfe von der Operation .sort()

int_list.sort()
print(int_list)

# Einfügen an einem Index, kein Überschreiben der Einträge

mixed_list.insert(0, "Gisela")
print(mixed_list)

# Wenn wir mehrere Elemente ans Ende einfügen wollen, können wir .extend() nehmen

mixed_list.extend(["Gerold", 8645312, 64.564, "-∞"])
print(mixed_list)
# Entfernen von Elementen kann auch wertbasiert sein,
# d.h. nach dem ersten Auftreten des übergebenen Wertes

mixed_list.remove("Gerold")
print(mixed_list)

# Werte der Liste löschen

mixed_list.clear()
print(mixed_list)



