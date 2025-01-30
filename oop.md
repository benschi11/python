# Objektorientierte Programmierung
Um Programmierung einfacher und vor allem übersichtlicher und wartbarer zu machen, wurden Klassen und Objekte eingeführt. Diese Programmierung nennt man **objektorientierte Programmierung**.

## Inhaltsverzeichnis

* [Klasse](#klasse)
* [Objekte](#objekte)
* [Konstruktor](#konstruktor)

## Klasse
Eine Klasse kann man sich wie einen Bauplan vorstellen. Nehmen wir z.B.: ein Auto: ein Auto hat eine Anzahl von Sitzen, eine Farbe, kann beschleunigen, ....
Alle diese Eigenschaften und Methoden kann man in einer Klasse zusammenfassen.

In diesem Example erstellen wir eine Klasse `Car` mit vorerst einer Eigenschaft `color`. Dafür verwenden wir das Keyword `class` und danach den Namen.
In dieser Klasse werden zwei Methoden definiert - ein Getter und ein Setter für Color. Der Getter erlaubt den Zugriff von Außen auf die Eigenschaft color und mit dem Setter lässt sich der Wert von außen ändern.

In jeder Methode, die zu einer Klasse gehört, müssen wir als ersten Parameter `self` eingeben. Eine genauere Erklärung dazu wird später folgen.

```python
class Car:

    # Getter für Color
    def getColor(self):
        return self.__color
    
    # Setter für Color
    def setColor(self, value):
        self.__color = value
```

## Objekte
Wir haben jetzt eine Klasse, also einen Bauplan für ein Auto. Jetzt möchten wir unterschiedliche Autos erstellen. Jedes Element, dass vom Typ `Car` ist, nennt man ein Objekt oder eine Instanz der Klasse `Car` - also eine wirkliche Realisierung.

Eine Realsierung wird einfach durch den Namen der Klasse und `()` dahinter durchgeführt. Diese muss natürlich in eine Variable gespeichert werden.
```Python
# Erstellt eine neue Instanz der Klasse `Car`
blueCar = Car()
blueCar.setColor("blue")

# Erstellt eine weitere Instanz der Klasse `Car`
redCar = Car()
redCar.setColor("red")

# Zugriff auf die Eigenschaften
print("Farbe des ersten Autos " + blueCar.getColor())
print("Farbe des zweiten Autos " + redCar.getColor())
```

Obwohl die beiden Objekte `blueCar` und `redCar` beide von der selben Klasse sind, haben beide von ihnen aber ihre eigenen Daten für die Eigenschaft.

## Konstruktor
Ein Konsturktor wird dann aufgerufen, wenn eine neue Instanz einer Klasse erstellt wird.

```python
blueCar = Car() # hier wird der Konstruktor aufgerufen
```
Diesen Konstruktor kann man selber in der Klassen definieren. In Python verwendet man dafür die `__init__` Methode. Erweitern wir unsere Klasse `Car` also um einen eigenen Konstruktor, welcher uns gleich beim Erstellen des Objektes die Farbe definiert lässt.

```python
class Car:

    def __init__(self, color): # color wird im Konstruktor übergeben
        self.setColor(color) # die Eigenschaft `color` der Klasse wird auf den übergebenen Wert gesetzt

    # Getter für Color
    def getColor(self):
        return self.__color
    
    # Setter für Color
    def setColor(self, value):
        self.__color = value
```
Nun müssen wir die Objekte vom Typ `Car` etwas anders erstellen. Der Konstruktor erwartet jetzt von uns nämlich ein zusätzliches Argument - die Farbe (`color`).
Daher kann dieser ganze Process vereinfacht werden:

```Python
blueCar = Car("blue")
redCar = Car("red")

print("Farbe des ersten Autos " + blueCar.getColor())
print("Farbe des zweiten Autos " + redCar.getColor())
```

Im Konstruktor können natürlich viele Werte übergeben werden z.B.: noch die Eigenschaft wie viele Türen das Auto besitzt.
```python
class Car:

    def __init__(self, color, doors): 
        self.setColor(color)
        self.setDoors(doors)

    def getDoors(self):
        return self.__doors

    def setDoors(self, value):
        self.__doors = value

    def getColor(self):
        return self.__color
    
    def setColor(self, value):
        self.__color = value
```

Um ein Objekt dieser Klasse zu erstellen müssen wir nun zwei Parameter übergeben (`color, doors`):

```Python
# Erstellt ein Auto mit der Farbe blau und 5 Türen
blueCar = Car("blue", 5)
# Erstellt ein weiteres Auto mit der Farbe rot und 3 Türen
redCar = Car("red", 3)
```
## Methoden
<mark style="background-color: #FFFF00">TODO: Hier fehlt noch etwas</mark>  
## Properties
<mark style="background-color: #FFFF00">TODO: Hier fehlt noch etwas</mark>  

## Dataclasses
Um nicht immer diese ganzen Properties schreiben zu müssen, gibt es eine sehr nützliche Erweiterung, die sich `DataClasses` nennt. Mit Hilfe dieses Paketes lassen sich Dataklassen viel einfacher implementieren.

Sollte das Paket noch nicht installiert sein, werden wir es mit Hilfe von `pip` installieren. Benutze dazu folgenden Befehl:
```
pip install dataclasses
```

Verlgleichen wir jetzt die beiden Arten: Bis jetzt mussten wir für jede Eigenschaft unserer Klasse in den meisten Fällen zwei Property Functions definieren. Nehmen wir z.B.: eine Klasse `Student` her.

```python
class student:
    def __init__(self, prename: str, surname: str) -> None:
        self.__prename = prename;
        self.__surname = surname;

    @property
    def prename(self) -> str:
        return self.__prename
    
    @prename.setter
    def prename(self, value) -> None:
        self.__prename = value;

    @property
    def surname(self) -> str:
        return self.__surname
    
    @surname.setter
    def surname(self, value) -> None:
        self.__surname = value;
    
    def __repr__(self) -> str:
        return f"Prename: {self.prename}, Surname: {self.surname}"

## Verwende die Klasse

s1 = student("Benedikt", "Neuhold")
s2 = student("Gerald", "Geier")

## Ausgabe der Objekte
print(s1)
print(s2)
``` 
Diese einfache Klasse, die nur Vor- und Nachnamen besitzt benötigt schon einige Zeilen Code. Schauen wir uns diese Klasse nun mit Hilfe der `dataclass` an.

```python
from dataclasses import dataclass

@dataclass
class student:
    prename: str
    surname: str

## Verwende die Klasse

s1 = student("Benedikt", "Neuhold")
s2 = student("Gerald", "Geier")

## Ausgabe der Objekte
print(s1)
print(s2)

```

Es lassen sich zum Beispiel auch Standardwerte definieren oder einzelne Eigenschaften aus dem Konstruktor herausnehmen.

```python
from dataclasses import dataclass, field

@dataclass
class student:
    id : int
    prename: str
    surname: str = "Mustermann" # default Wert für surname


## Verwende die Klasse

s1 = student(1, "Benedikt", "Neuhold")
s2 = student(2, "Gerald") # default Wert "Mustermann" wird verwendet.

## Ausgabe der Objekte
print(s1)
print(s2)
```

Weiter Informationen zur `dataclasses` findest du auf deren [Webseite](https://docs.python.org/3/library/dataclasses.html).

## Vererbung
In allen höheren Programmiersprachen gibt es das Konzept der Vererbung. Dies ist nützlich, damit man bei unterschiedlichen Klassen, die aber viele Gemeinsamkeiten haben, weniger Code schreiben muss.
Nehmen wir z.B.: die Klasse `Auto` und `Fahrrad`. Beide Klassen gehören zur Überkategorie Fahrzeug und beide haben eine Geschwindigkeit und können `bremsen` und `beschleunigen`.

Daher ist es sinnvoll, dass wir eine 'Basisklasse' erstellen, die alle diese Gemeinsamkeiten abbildet. Nennen wir die Klasse `Fahrzeug`. Sie implementiert alle gemeinsamen Eigenschaften und Methoden. Auserdem stellt sie eine Methode `info` bereit, wo je nach Klasse jeweils die Informationen ausgegeben werden. Hier wird die Funktionsdefinition in der Basisklasse definiere, die implementierung muss aber in der konkreten Klasse erfolgen. Sollte das nicht geschehen, würde zur Laufzeit ein `NotImplementedError` - Fehler auftreten.

```python
class Fahrzeug:
    def __init__(self, geschwindigkeit=0):
        self.geschwindigkeit = geschwindigkeit

    def beschleunigen(self, delta):
        self.geschwindigkeit += delta
        print(f"Geschwindigkeit um {delta} erhöht auf {self.geschwindigkeit} km/h")

    def bremsen(self, delta):
        self.geschwindigkeit -= delta
        if self.geschwindigkeit < 0:
            self.geschwindigkeit = 0
        print(f"Geschwindigkeit um {delta} verringert auf {self.geschwindigkeit} km/h")

    def info(self):
        raise NotImplementedError("Subklassen müssen diese Methode implementieren")
```

Schreiben wir nun unsere beiden konkreten Klassen `Fahrrad` und `Auto`.

```python
# Abgeleitete Klasse (Kindklasse)
class Auto(Fahrzeug):
    def __init__(self, geschwindigkeit=0, tankinhalt=50):
        super().__init__(geschwindigkeit)
        self.tankinhalt = tankinhalt

    def info(self):
        return (f"Auto: Geschwindigkeit = {self.geschwindigkeit} km/h, "
                f"Tankinhalt = {self.tankinhalt} Liter")

    def tanken(self, liter):
        self.tankinhalt += liter
        print(f"Getankt! Tankinhalt ist jetzt {self.tankinhalt} Liter")
```

```python
    # Abgeleitete Klasse (Kindklasse)
class Fahrrad(Fahrzeug):
    def __init__(self, geschwindigkeit=0, reifendruck=2.5):
        super().__init__(geschwindigkeit)
        self.reifendruck = reifendruck

    def info(self):
        return (f"Fahrrad: Geschwindigkeit = {self.geschwindigkeit} km/h, "
                f"Reifendruck = {self.reifendruck} bar")

    def pumpen(self, bar):
        self.reifendruck += bar
        print(f"Reifen aufgepumpt! Reifendruck ist jetzt {self.reifendruck} bar")
```

Nun können wir Objekte von unseren konkreten Klassen anlegen. Man wird dann sehen, dass diese auch die Methoden `bremsen` und `beschleunigen` aus der Basisklasse besitzen. Zusätzlich verfügen sie aber auch um die eigenen Methoden `tanken` und `pumpen`, die jeweils nur das `Auto` oder das `Fahrrad` besitzt.

```python
# Objekte erstellen
auto = Auto(geschwindigkeit=30, tankinhalt=40)
fahrrad = Fahrrad(geschwindigkeit=15, reifendruck=2.0)

# Methoden aufrufen
print(auto.anzeigen())  # Ausgabe: Auto: Geschwindigkeit = 30 km/h, Tankinhalt = 40 Liter
print(fahrrad.anzeigen())  # Ausgabe: Fahrrad: Geschwindigkeit = 15 km/h, Reifendruck = 2.0 bar

auto.beschleunigen(20)  # Ausgabe: Geschwindigkeit erhöht auf 50 km/h
fahrrad.bremsen(5)  # Ausgabe: Geschwindigkeit verringert auf 10 km/h

auto.tanken(10)  # Ausgabe: Getankt! Tankinhalt ist jetzt 50 Liter
fahrrad.pumpen(0.5)  # Ausgabe: Reifen aufgepumpt! Reifendruck ist jetzt 2.5 bar

print(auto.anzeigen())  # Ausgabe: Auto: Geschwindigkeit = 50 km/h, Tankinhalt = 50 Liter
print(fahrrad.anzeigen())  # Ausgabe: Fahrrad: Geschwindigkeit = 10 km/h, Reifendruck = 2.5 bar
```