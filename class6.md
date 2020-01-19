# Python Kurs - 6. Klasse

## Objektorientierte Programmierung

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

- [ ]Beispiele aus dem Unterricht hinzufügen 

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

- [ ]Beispiele aus dem Unterricht hinzufügen 

### Gesamten Inhalt auf einmal lesen
Es ist auch möglich den gesamten Inhalt einer Datei mit einem Befehl in eine Liste einzulesen. Dies wird durch ausführen des `.readlines()` Befehls auf das geöffnete Dateiobjekt erreicht.

Dieser Code speichert den gesamten Inhalt der Datei `6a.txt` in der Liste `students`. Jede Zeile wird in einen Listeneintrag gespeichert.
```python
students = open("6a.txt").readlines()
```

- [ ]Beispiele aus dem Unterricht hinzufügen 