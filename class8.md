# Grafische Oberflächen mit PyQT

## Inhaltsverzeichnis

* [Installation](#installation)
* [Hello World](#hello-world)

Um grafische Oberflächen zu erstellen gibt es mehrere Möglichkeiten. Wir werden uns in der Schule mit QT genauer mit pyQT beschäftigen.
## Installation
### Windows
Der einfachste Weg pyQT 6 unter Windows zu installieren ist über den in Python integrierten Packagemanager `pip`:

```
pip install pyqt6
```

### OS X
Unter OS X wird das Tool `brew` benötigt.

```
brew install pyqt
```


### Linux (Ubuntu)
Unter einer Ubuntu Distor mit dem Packagemanager `apt-get` wird pyQT folgendermaßen installiert:

```
sudo apt-get install python3-pyqt6
```

## Hello World
Mit diesem Programm möchten wir testen, ob alle installierten Komponenten funktionieren.

Erzeuge eine leere Python Datei und nenne sie `qt-HelloWorld.py`.

Zuerst müssen wir **alle notwendigen Libraries** importierten:
```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot
```

Danach definieren wir das Hauptfenster und die ersten Elemente:

```python
app = QApplication(sys.argv)
widget = QWidget()

textLabel = QLabel(widget)
textLabel.setText("Hello World!")
textLabel.move(110,85)

widget.setGeometry(50,50,320,200)
widget.setWindowTitle("PyQt5 Example")
widget.show()
sys.exit(app.exec_())
```
