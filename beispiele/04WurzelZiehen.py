import math; # importiert das ganze Mathe Modul
a = float(input("Bitte geben Sie eine Zahl ein:"));

wurzel = math.sqrt(a);
print("Die Wurzel von " + str(a) + " ist " + str(wurzel));

hochFünf = math.pow(a,5);
print(str(a) + " hoch 5 ergibt " + str(hochFünf));