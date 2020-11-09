# Python Kurs - 5. Klasse

## Einführung

## Variablen und Datentypen

Eine Variable ist in jeder Programmiersprache einfach ein Behälter, der gewisse Werte speichern kann (z.B.: Text, ganze Zahlen, Zahlen mit Komma). Eine Variable besitzt einen **Namen**, einen **Datentyp** und einen **Wert**. 

### Name

Der Name einer Variable ist **frei wählbar**. Allerdings sollte man sich angewöhnen, dass man keine Umlaute verwendet und auch mit Sonderzeichen eher sparsam umgeht.

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
kommazahl = float(input("Bitte geben Sie Ihre Größe in m ein:")) # konvertiert die Eingabe in eine Dezimalzahl
summe = str(243.4) # konvertiert den float-Wert 243.4 in einen Text
```

## IF-Anweisung
In der Softwareentwicklung muss oft etwas überprüft werden. Dies geschieht in allen Programmiersprachen mit der `if-Anweisung`. 
Diese hat immer folgende Syntax:
```python
if <Überprüfung> :
  <Code wenn Überprüfung korrekt>
```

Sollte es sich um eine "Wenn - dann - ansonsten" - Entscheidung handeln, kann die `if-Anweisung` noch um einen `else`-Ast erweitert werden.
```python
if <Überprüfung> :
  <Code wenn Überprüfung korrekt>
else:
  <Code wenn Überprüfung NICHT korrekt>
```

Sollten mehr als zwei Möglichkeiten vorhanden sein, gibt es auch die Möglichkeit von `elif` (else - if).
```python
if <Überprüfung 1> :
  <Code wenn Überprüfung 1 korrekt>
elif <Überprüfung 2>:
  <Code wenn Überprüfung 2 korrekt>
else:
  <Code wenn Überprüfung 1 und Überprüfung 2 NICHT korrekt>
```

## Liste (Arrays)
Eine Liste ist in der Programmierung eine Variable, in der mehrere Werte seperiert voneinander gespeichert werden können.
Zum Beispiel kann ich eine Variable ```Obst``` erzeugen, die alle Obstsorten gespeichert hat, die ich gerade zuhause habe.
####Syntax
```python
obst = ["Orange", "Apfel", "Kiwi"]
```
In diesem Fall werden in der Variable ```obst``` 3 Werte gespeichert - Orange, Apfel und Kiwi. Um auf die einzelnen Werte dieser Liste zuzugreifen muss die eckige Klammer (*STRG + SHIFT + 8* **ODER** ALT GR + 8 ) verwendent werden. In der Klammer wird der sogenannte "Index" angegeben --> **Wichtig:** Der Index startet beim ersten Element der Liste immer mit 0.
```python
print(obst[0])
```
*Ausgabe:*
```
Orange
```


## Schleifen
Wenn man als Programmierer gewisse Dinge öfter wiederholen möchte oder immer das Gleiche mit unterschiedlichen Dingen machen möchte, dann benötigt man Schleifen.
In Python gibt es zwei Schleifen - die for-Schleife und die while-Schleife.

### for-Schleife
Die for-Schleife in Python benötigt eine Liste. Für jeden Eintrag der Liste wird ein Schleifendurchgang durchgeführt.

#### Syntax
```python
for <Variable> in <Liste>:
  <Schleifendurchgang>
```

#####Beispiel Obstsalat:
```python
obstsalat = ["Apfel", "Banane", "Kiwi", "Ananas"]
for obst in obstsalat:
  print("Schneide " + obst)
```
*Ausgabe:*
```
Schneide Apfel
Schneide Banane
Schneide Kiwi
Schneide Ananas
```

Da wir sehr oft in der Programmierung ein Schleife von 1 bis x laufen lassen müssen gibt es hierfür in Python einen Befehl um eine Liste von 1 bis x zu generieren. Dieser Befehl nennt sich ```range(1,x)``` und hat eine bestimmte Eigenheit --> er generiert eine Liste von 1 bis x-1, d.h. die letzte Zahl selber ist nicht mehr in der Liste dabei.
```python
a = list(range(1,4)) # generiert eine Liste von 1 bis 3 => a=[1,2,3]
b = list(range(1,10)) # generiert eine Liste von 1 bis 9
c = list(range(1,101)) # generiert eine Liste von 1 bis 100
```

#####Beispiel Zählen:

```python
count = 0
for i in range(1,51):
  count = count + 1

print(count)
```
*Ausgabe:*
```
50
```

### while-Schleife

Oftmals kommt es beim Programmieren auch vor, dass ich von Beginn an nicht weiß, wie oft meine Schleife laufen muss - sondern ich möchte, dass sie so lange läuft, so lange eine Bedingung erfüllt ist. Diese Ausgangslage kann mit der for-Schleife nur sehr schwer umgesetzt werden, daher gibt es eine weitere Schleife - die while-Schleife.

#### Syntax
```python
while <Bedingung>:
  <Schleifendurchgang>
```

Ein sehr häufiges Beispiel ist, dass der Benutzer so lange nach einer Eingabe gefragt wird, bis er sie richtig eingibt.

```Python
eingabe = input("Bitte geben Sie 'J' ein:")
while eingabe != "J":
  eingabe = input("Bitte geben Sie 'J' ein:")
```
Diese Schleife wird also so lange ausgeführt, so lange die Bedingung ```eingabe != "J"``` erfüllt ist, also in der Variable ```eingabe``` nicht "J" steht.

Viele Programmiere mögen es nicht, dass im obrigen Beispiel die Zeile 1 und 3 doppelt geschrieben werden müssen. Daher arbeiten viele mit Hilfe eines Tricks: Sie erzeugen eine Endlosschleife und prüfen in jedem Schleifendurchgang händisch ob die Bedingung nicht mehr erfüllt ist - sollte dies der Fall sein wird die Schleife mit `break` verlassen.

```python
for True: # Endlosschleife
  eingabe = input("Bitte geben Sie ein 'J' ein:")
  if eingabe == "J":
    break #verlasse die Schleife
```

Du kannst gerne beide Arten verwenden - je nach dem welche dir besser gefällt.