# Python Kurs - 6. Klasse

## Funktionen
In vielen Fällen möchte man einen gewissen Codeblock gerne an verschiedenen Stellen wiederverwenden. In diesem Fall eigenen sich Funktionen sehr gut. Eine Funktion kann man sich wie ein Stück Code vorstellen, dass bei Aufruf der Funktion immer wieder durchgeführt wird.

### Funktionen ohne Parameter und Rückgabewert

Das einfachste Beispiel ist eine Trennline. Ich möchte Teile meiner Ausgabe mit Hilfe von Trennzeichen abtrennen. Dafür wird eine Funktion `trennlinie` definieren:
```python
def trennlinie():
  print("-"*20)
```
Code der in einer Funktion definiert ist, wird standardmäßig nicht ausgeführt. Die Funktion muss erst mit Hilfe ihres Namens und `()` aufgerufen werden:

```python
def trennlinie():
  print("-"*20)

trennlinie()
print("Ich lerne geraden Funktionen")
trennlinie()
```
<em>**Ausgabe:**</em>
```
--------------------
Ich lerne geraden Funktionen
--------------------
```

Man kann es sich jetzt so vorstellen, dass anstatt von `trennlinie()` der Code aus der Funktion `trennlinie` ausgeführt wird. 

Dies hat natürlich den Vorteil, dass wenn ich das Trennzeichen ändern möchte, ich dies nur genau an einer Stelle machen muss.
Änderung des Trennzeichens auf "#":
```python
def trennlinie():
  print("#"*20)

trennlinie()
print("Ich lerne geraden Funktionen")
trennlinie()
```

<em>**Ausgabe:**</em>
```
####################
Ich lerne geraden Funktionen
####################
```

### Funktionen mit Rückgabewert, aber ohne Parameter
Wir wollen eine Funktion schreiben, welche je nach aktueller Uhrzeit eine Begrüßung zurückgibt. Die Funktion hat den Namen `greeting` und gib der aufrufenden Stelle, in diesem Fall, einen String zurück.
```python
from datetime import datetime

# ------------- Beginn der Funktion -----------
def greeting():
    current_time = datetime.now()

    if current_time.hour < 9:
        return "guten Morgen"
    elif current_time.hour < 12:
        return "schönen Vormittag"
    elif current_time.hour < 15:
        return "guten Mittag"
    elif current_time.hour < 18:
        return "schönen Nachmittag"
    elif current_time.hour < 22:
        return "schönen Abend"
    else:
        return "Gute Nacht"
# ------------- Ende der Funktion -----------
    
name = input("Geben Sie Ihren Namen ein: ")
begruessung = greeting()

print("Lieber " + name + " ich wünsche " + begruessung)
```

## Dateioperationen

### Lesen einer Datei

Um in Python eine Datei zu öffnen muss die Funktion `open()` verwendet werden. Diese Funktion erhält den Pfad zur zu lesenden Datei und mit welchen Rechten die Datei geöffnet werden soll.

Zum Beispiel würde dieser Code die Datei nur mit Leseberechtigung (=read) öffnen. In diesem Fall könnte man das `"r"` sogar weglassen, da dies der Standardwert ist.

```python
students_file = open("6a.txt", "r")
```

Wenn ich die Datei nun geöffnet wurde, dann ist es möglich die Datei Zeile für Zeile einzulesen. Dies ist ganz einfach mit einer **for-Schleife** über das Dateiobjekt möglich.

```python
students_file = open("6a.txt")
for line in students_file:
    print line
students_file.close()
```

Wichtig ist es auch, am Ende des Lesevorgangs die Datei wieder zu schließen. Dies ist mit `.close()` direkt auf das Dateiobjekt möglich.


### Schreiben in eine Datei

Um in eine Datei etwas zu schreiben, muss diese auch mit Schreibrechten geöffnet werden. Dies passiert durch Angabe des Parameters `"w"` an die `open()` Funktion. Ansonsten passiert alles analog zum lesen.

Hier noch eine Übersicht aller für uns wichtigen Modi, mit der eine Datei geöffnet werden kann:

Mode | Beschreibung
-----|--------------
`'r'`| Öffnet eine Datei zum Lesen
`'w'`| Öffnet eine Datei zum Schreibe. Sollte die Datei nicht existieren, so wird sie erstellt. Existiert sie, wird der Inhalt überschrieben.
`'x'`| Öffnet eine Datei für exklusive Erstellung, d.h. wenn die Datei bereits existiert wird ein Fehler ausgegben
`'a'`| Öffnet die Datei im Hinzufügemodus. D.h. die Inhalte werden zur bestehenden Datei hinzufügt. Ist die Datei nicht vorhanden, wird sie erstellt.

Der nachfolgende Code schreibt in die Datei einfach die Zahlen von 1 bis 10.

```python
datei = open("numbers.txt","w")
for i in range(1,11):
    datei.write(str(i) + "\n")
datei.close()
```

### Gesamten Inhalt auf einmal lesen
Es ist auch möglich den gesamten Inhalt einer Datei mit einem Befehl in eine Liste einzulesen. Dies wird durch ausführen des `.readlines()` Befehls auf das geöffnete Dateiobjekt erreicht.

Dieser Code speichert den gesamten Inhalt der Datei `6a.txt` in der Liste `students`. Jede Zeile wird in einen Listeneintrag gespeichert.
```python
students = open("6a.txt").readlines()
```

### Beispiele

## Aufbau einer Datei
Um Inhalte aus einer Datei zu lesen oder in eine Datei zu speichern ist es sinnvoll, sich eine gute Datenstruktur zu überlegen. Die dafür sehr häufige Struktur ist das csv-Schema. Hierbei wird für jeden Datensatz eine eigene Zeile angelegt und innerhalb des Datensatzes wird per ";" oder "," getrennt.

```
Nachname;Vorname;Alter
Neuhold;Benedikt;32
Maier;Sepp;45
Huber;Walter;28
```

Diese Struktur muss mit Python nach dem Einlesen noch in die Einzelteile zerlegt werden. Dies ist über die Funktion `split()` möglich. Diese Funktion teilt einen String nach einem vorgegebenen Trennzeichen auf und gibt jeden Eintrag in einer Liste zurück.

```python
zeile = "Neuhold;Benedikt;Alter"
nb = zeile.split(";")
print(nb)
```
Dieser Sourcecode teilt den String `zeile` nach jedem `;` auf und speichert den Eintrag in eine Liste. Dann wird diese Liste in `nb` gespeichert und ausgegeben. Ausgabe: `['Neuhold', 'Benedikt', 'Alter']`

