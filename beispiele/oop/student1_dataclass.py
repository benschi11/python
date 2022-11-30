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

s1.prename = "Hansi"