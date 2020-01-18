import random;
name = input("Bitte geben Sie Ihren Namen ein:");

# Note für Mathematik
mathe = random.randint(1,5);

#Note für Deutsch
deutsch = random.randint(1,5);

#Note für Englisch
englisch = random.randint(1,5);

#Ausgabe
print("Noten für " + name +":");
print("Mathematik:\t" + str(mathe));
print("Deutsch: \t" + str(deutsch));
print("Englisch: \t" + str(englisch));