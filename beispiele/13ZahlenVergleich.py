# Der Benutzer soll zwei Dezimalzahlen eingeben. Und es wird die
# größere Zahl ausgegeben.

z1 = float(input("Bitte geben Sie die erste Zahl ein:"));
z2 = float(input("Bitte geben Sie die zweite Zahl ein:"));

# Version 1
if z1 > z2:
    print("Die Zahl " + str(z1) + " ist größer als " + str(z2));
else:
    print("Die Zahl " + str(z2) + " ist größer als " + str(z1));

print("----------------------- Zusatz -----------------------");
# Zusatz:
if z1 > z2:
    print("Die Zahl " + str(z1) + " ist größer als " + str(z2));
elif z2 > z1:
    print("Die Zahl " + str(z2) + " ist größer als " + str(z1));
else:
    print("Die beiden Zahlen sind gleich groß!")

