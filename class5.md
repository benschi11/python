# Python Kurs - 5. Klasse

## Einführung

## Variablen und Datentypen

Eine Variable ist in jeder Programmiersprache einfach ein Behälter, der gewisse Werte speichern kann (z.B.: Text, ganze Zahlen, Zahlen mit Komma). Eine Variable besitzt einen **Namen**, einen **Datentyp** und einen **Wert**. 

### Name

Der Name einer Variable ist **frei wählbar**. Allerdings sollte man sich angewöhnen, dass man keine Umlaute verwendet und auch mit Sonderzeichen eher sparsamer umgeht.

### Datentyp

Man muss dem Computer sagen, welche Art von Daten wir gerne speichern würden. Das hat den Grund, da sonst der Computer nicht weiß wie er z.B.: die "+" Operation durchführen soll.

Muss er eine "+" Operation mit zwei Zahlen durchführen werden diese addiert, allerdings wird eine "+" Operation auf zwei Texte angewand, so werden diese beiden Texte einfach aneinandergehängt.

Wir beschäftigen uns hauptsächlich mit folgendn Datentypen:

* **string** : Text
* **integer** : ganze Zahlen
* **float** : Kommazahlen
* **bool** : kann nur zwei Werte (Richtig / Falsch) annehmen

### Wert

Als Wert der Variable bezeichnet man den aktuellen Wert (=Inhalt) den diese Variable gerade bestitzt.

Um eine Variable mit dem Namen 'zahl', dem Datentyp integer und dem Wert 3 anzulegen muss man folgenden Python Code schreiben:

```python
zahl = 3
```

Hier noch einige andere Variablen mit dazugehörigen Namen, Datentyp und Wert als Kommentar

```python
a1 = 7              # Name: a1, Datentyp: integer, Wert: 7
kommazahl = 3.11    # Name: kommazahl, Datentyp: float, Wert: 3.11
c1 = "Hallo Welt"   # Name: c1, Datentyp: string, Wert: "Hallo Welt"
```

### Beispiele:

* <a href="https://github.com/benschi11/python-5/blob/master/beispiele/01HelloWorld.py">01HelloWorld.py</a>

## Einlesen und Ausgabe

Um in Python etwas auf die Console zu schreiben muss die Funktino **print** verwendet werden.

Dieser Code gibt auf der Console "Hallo Welt" aus.

```python
print("Hallo Welt")
```

Um etwas vom Benutzer einzulesen bzw. abzufragen, muss die Funktion **input** verwendet werden. Diese Funktion gibt die Eingabe des Benutzers zurück. Wichtig ist hierbei, dass der zurückgegebenen Wert immer als **Text (string)** zurückgegeben werden - unabhängig davon was eingegeben wird.

Dieser Code fordert den Benutzer auf sein Alter einzugeben und liest den eingegebenen Wert ein und speichert ihn in der Variable *eingabe* als Text.

```python
eingabe = input("Bitte geben Sie Ihr Alter ein:") # in diesen Fall ist die Variable eingabe vom Typ string
```

Eigentlich wissen wir jedoch alle, dass das Alter eigentlich eine ganze Zahl ist. Dies müssen wir dem Computer mitteilen. Der Begriff einen Variable oder einen Wert in einen anderen Datentyp zu ändern lautet **konvertieren**.

### Konvertieren

Wenn ich einen Wert für eine Variable setze und der Datentyp dieses Wertes für meine Zwecke ungeeignet ist, so kann ich dem Computer sagen, dass er diesen Wert versuchen soll zu konvertieren (umzuwandeln). Dies ist in Python einfach durch das Voranstellen des gewünschten Datentyps als Funktion (mit runden Klammern) möglich.

In diesem Beispiel wird die Eingabe (die vom Datentyp string ist) in einen Integer konvertiert. Dies geschieht Ausführen der Funktion *int()*.

```python
eingabe = int(input("Bitte geben Sie Ihr Alter ein:"))
```

Weitere Konvertierungsmöglichkeiten sind folgende:

```python
kommazahl = float(input("Bitte geben Sie Ihre Größe in m ein:"))
summe = str(243.4)
```

## IF-Anweisung
