# Objektorientierte Programmierung
Um Programmierung einfacher und vor allem übersichtlicher und wartbarer zu machen, wurden Klassen und Objekte eingeführt. Diese Programmierung nennt man **objektorientierte Programmierung**.

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

