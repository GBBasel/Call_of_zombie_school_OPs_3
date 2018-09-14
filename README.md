# Call_of_Zombie_school_OPs_3

## Grundstruktur des Spiels:

Die Erde wird von einer andauernden Seuche bedroht. Die Infizierten verlieren ihr Bewusstsein und allen Willen. Es gibt nur noch eins: Jemanden beissen und den Keim übertragen!
Doch nicht alle Menschen ergeben sich so einfach. Ein paar mutige Helden haben sich bewaffnet und es sich zum Ziel gemacht, die Erde zu retten.

Die Hauptidee ist simpel: Auf der einen Seite steht zu Anfang die Hauptfigur, auf der anderen strömen die Zombies heran. Die Hauptfigur kann sich in vier Richtungen bewegen, gesteuert durch die Pfeiltasten, und schiessen, mit Hilfe der Spacetaste. Sobald geschossen wird, erscheint eine Kugel. Wenn diese einen Zombie trifft, verschwinden beide, ausserdem wird ein Punkt hinzugezählt. Die Maximalpunktzahl beträgt 100. Wenn ein Zombie aber den Menschen berührt, dann wird er selbst zum Zombie und das Spiel ist vorbei. Dazu spielt eine nervige 8-bit-Melodie.

![Startbildschirm](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/start.jpg)
Startbildschirm mit Erklärungen zum Spielablauf

## Programmieren:

Zunächst haben wir die Actors definiert. Es gibt einen Menschen (human), die Zombies (zombie) und eine Kugel (bullet). Ausserdem gibt es eine Klasse für den Startbildschirm (start) und eine Klasse, die die Kollissionen überwacht. So lange das Fenster geöffnet ist, werden Punkte zusammengezählt und Leben abgezogen.

### Human

![Human](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/Human.png)

Er erscheint zu Beginn des Spiels an der linken Seite des Spielfelds. Mit den vier Pfeiltasten lässt er sich bewegen, wobei er sich immer fünf Pixel bewegt. Sobald er sich aus dem Spielfeld heraus bewegt, wird er an den Rand zurückgesetzt. Somit wird verhindert, dass er das Spielfeld verlässt.

### Bullet

![Bullet](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/Bullet.png)

Die Kugel wird durch die Spacetaste erzeugt und  entsteht immer dort, wo sich der Mensch gerade befindet. Sie fragt beim erzeugen die Koordinaten des Human ab. Es gibt eine Verzögerung von dreissig Millisekunden zwischen den Schüssen, damit mit einem Drücken der Taste nicht mehrere Zombies vernichtet werden können.

### Zombies

![Zombie](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/Zombie.png)

Die Zombies werden ausserhalb des Spielfeldes an zufälligen Orten erzeugt und gehen nach links. Wenn sie den Menschen berühren, ist das Spiel vorbei.


![Boss](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/boss.png)

Der Boss ist der letzte Zombie, der erscheint. Er ist eine Art mutierte Wassermelone. Er lässt sich so wie die anderen Zombies vernichten.





## Schwierigkeiten

Beim Programmieren des Spiel stiessen wir auf verschiedene Schwierigkeiten.

* Zunächst einmal funktionierten die Collissionevents nicht so, wie uns das durch die Tigerjythonseite erklärt worden war. Wir mussten eine andere Methode verwenden, um zum Ziel zu kommen.

* Die Bullet brauchte einen Timer, damit nicht mehr wie eine Kugel auf einmal abgefeuert werden kann.

* Die Titelmelodie musste so angepasst werden, dass sie irgendwann aufhört.

* Das Laggen konnte durch einen print-Befehl gelöst werden. Wir wissen nicht, wieso.

* Die Collissionboxes brauchten eine spezielle Konstruktion.

* Der Mensch konnte zunächst das Spielfeld verlassen, das konnte aber durch einen Befehlsblock geregelt werden.

* Der Startbildschrim brauchte einiges an Kreativität, einen neuen Actor und eine Verzögerung _delay()_.



## Der Code

```python
from gamegrid import *
from random import randint
import time
```

Alle Funktionen von Gamegrid, _randint_ und time werden importiert.

```python
nbLifes = 3  #Leben
 nbKillKount = 0  #Punkte
 F = 0   # Bullet wird entfernt, wenn F < 0 (nach Ende des Spiel kann nicht mehr geschossen werden)
 U = 80  # Zombies erste Welle
 V = 19  # Zombies zweite Welle
 n = 1  # Boss
```


