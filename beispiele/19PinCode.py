import random;
# Erstelle einen zufälligen 4 stelligen PinCode
a = random.randint(0,9);
b = random.randint(0,9);
c = random.randint(0,9);
d = random.randint(0,9);

# Ausgabe
print("Ihr PinCode: " + str(a) + str(b) + str(c) + str(d));

code = ""
a = str(random.randint(0,9))
code = code + a
a = str(random.randint(0,9))
code = code + a
a = str(random.randint(0,9))
code = code + a
a = str(random.randint(0,9))
code = code + a
print("Ihr PinCode: " + code)

# Erstelle einen PIN Code, mit der Länge die der Benutzer eingibt
lenght = int(input("Geben Sie bitte die Länge Ihres Pin Codes ein:"))

code = ""
for i in range(0,lenght):
    z = str(random.randint(0,9)) # erstellen der Zufallszahl + konvertieren zu string
    code = code + z
print(code)
