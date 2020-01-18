import math

# Einlesen
weight = float(input("Bitte geben Sie ihr Gewicht in kg ein:"));
height = float(input("Bitte geben Sie ihre Größe in m ein:"));

# Berechnen
#bmi = weight / math.pow(height,2);
bmi = weight / (height*height);

# Ausgabe
print("Ihr BMI ist " + str(bmi));

if bmi < 18:
    print("Sie sollten etwas mehr essen!");
elif bmi <=24:
    print("Behalten Sie ihr Essverhalten bei!");
else:
    print("Sie sollten weniger naschen!");
