# Benutzer gibt eine Zahl ein:
a = int(input("Bitte geben Sie eine Zahl ein"))

summe = 0
# Gib alle Zahlen von 1 bis zur eigebenen Zahl aus:
for i in range(1, a+1):
    print(i)
    summe = summe + i

# Zusatz: Gib die Summe dieser Zahlen aus
print("Summe:" + str(summe))

# Mittelwert
mittelwert = summe / a;
print("Mittelwert: " + str(mittelwert))