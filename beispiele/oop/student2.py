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