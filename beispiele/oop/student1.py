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