# Eingabe des Benutzers
weg = float(input("Bitte gib deinen zurückgelegten Weg ein:"));
zeit = float(input("Wie lange bist du gefahren?"));

# Durchschnittsgeschwindigkeit berechnen
v = weg / zeit;

# Ausgabe zur Reisegeschwindigkeit
if v > 100:
    print("Du bist zu schnell");
elif v >= 50:
    print("Du hast eine angenehme Reisegeschwindigkeit gewählt");
else:
    print("Du bist sehr langsam unterwegs gewesen");

