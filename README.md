# Call_of_Zombie_school_OPs_3

## Grundstruktur des Spiels:

Die Erde wird von einer andauernden Seuche bedroht. Die Infizierten verlieren ihr Bewusstsein und allen Willen. Es gibt nur noch eins: Jemanden beissen und den Keim übertragen!
Doch nicht alle Menschen ergeben sich so einfach. Ein paar mutige Helden haben sich bewaffnet und es sich zum Ziel gemacht, die Erde zu retten.

Die Hauptidee ist simpel: Auf der einen Seite steht zu Anfang die Hauptfigur, auf der anderen strömen die Zombies heran. Die Hauptfigur kann sich in vier Richtungen bewegen, gesteuert durch die Pfeiltasten, und schiessen, mit Hilfe der Spacetaste. Sobald geschossen wird, erscheint eine Kugel. Wenn diese einen Zombie trifft, verschwinden beide, ausserdem wird ein Punkt hinzugezählt. Die Maximalpunktzahl beträgt 99. Wenn ein Zombie aber den Menschen berührt, dann wird er selbst zum Zombie und das Spiel ist vorbei. Dazu spielt eine nervige 8-bit-Melodie.

![Startbildschirm](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/start.jpg)
Startbildschirm mit Erklärungen zum Spielablauf

## Programmieren:

Zunächst haben wir die Actors definiert. Es gibt einen Menschen (human), die Zombies (zombie) und eine Kugel (bullet). Ausserdem gibt es eine Klasse für den Startbildschirm (start) und eine Klasse, die die Kollissionen überwacht.

### Human

![Startbildschirm](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/Human.png)

Er erscheint zu Beginn des Spiels an der linken Seite des Spielfelds. Mit den vier Pfeiltasten lässt er sich bewegen, wobei er sich immer fünf Pixel bewegt. Sobald er sich aus dem Spielfeld heraus bewegt, wird er an den Rand zurückgesetzt. Somit wird verhindert, dass er das Spielfeld verlässt.

### Bullet

![Startbildschirm](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/Bullet.png)

Die Kugel wird durch die Spacetaste erzeugt und  entsteht immer dort, wo sich der Mensch gerade befindet. Sie fragt beim erzeugen die Koordinaten des Human ab. Es gibt eine Verzögerung von dreissig Millisekunden zwischen den Schüssen, damit mit einem Drücken der Taste nicht mehrere Zombies vernichtet werden können.

### Zombies

![Startbildschirm](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/Zombie.png)

Die Zombies werden ausserhalb des Spielfeldes an zufälligen Orten erzeugt und gehen nach links. Wenn sie den Menschen berühren, ist das Spiel vorbei.


![Startbildschirm](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/boss.png)

Der Boss ist der letzte Zombie, der erscheint. Er ist eine Art mutierte Wassermelone.





## Schierigkeiten

Beim Programmieren des Spiel stiessen wir auf verschiedene Schwierigkeiten. Zunächst einmal funktionierten die Collissionevents nicht so, wie uns das durch die Tigerjythonseite erklärt worden war.
