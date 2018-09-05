# Call_of_Zombie_school_OPs_3

## Grundstruktur des Spiels:

Die Erde wird von einer andauernden Seuche bedroht. Die Infizierten verlieren ihr Bewusstsein und allen Willen. Es gibt nur noch eins: Jemanden beissen und den Keim �bertragen!
Doch nicht alle Menschen ergeben sich so einfach. Ein paar mutige Helden haben sich bewaffnet und es sich zum Ziel gemacht, die Erde zu retten.

Die Hauptidee ist simpel: Auf der einen Seite steht zu Anfang die Hauptfigur, auf der anderen str�men die Zombies heran. Die Hauptfigur kann sich in vier Richtungen bewegen, gesteuert durch die Pfeiltasten, und schiessen, mit Hilfe der Spacetaste. Sobald geschossen wird, erscheint eine Kugel. Wenn diese einen Zombie trifft, verschwinden beide, ausserdem wird ein Punkt hinzugez�hlt. Die Maximalpunktzahl betr�gt 99. Wenn ein Zombie aber den Menschen ber�hrt, dann wird er selbst zum Zombie und das Spiel ist vorbei. Dazu spielt eine nervige 8-bit-Melodie.

![Startbildschirm](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/start.jpg)
Startbildschirm mit Erkl�rungen zum Spielablauf

## Programmieren:

Zun�chst haben wir die Actors definiert. Es gibt einen Menschen (human), die Zombies (zombie) und eine Kugel (bullet). Ausserdem gibt es eine Klasse f�r den Startbildschirm (start) und eine Klasse, die die Kollissionen �berwacht.

### Human

Er erscheint zu Beginn des Spiels an der linken Seite des Spielfelds. Mit den vier Pfeiltasten l�sst er sich bewegen, wobei er sich immer f�nf Pixel bewegt. Sobald er sich aus dem Spielfeld heraus bewegt, wird er an den Rand zur�ckgesetzt. Somit wird verhindert, dass er das Spielfeld verl�sst.

### Bullet

Die Kugel wird durch die Spacetaste erzeugt und  entsteht immer dort, wo sich der Mensch gerade befindet. Sie fragt beim erzeugen die Koordinaten des Human ab. Es gibt eine Verz�gerung von dreissig Millisekunden zwischen den Sch�ssen, damit mit einem Dr�cken der Taste nicht mehrere Zombies vernichtet werden k�nnen.

### Zombies







## Schierigkeiten

Beim Programmieren des Spiel stiessen wir auf verschiedene Schwierigkeiten. Zun�chst einmal funktionierten die Collissionevents nicht so, wie uns das durch die Tigerjythonseite erkl�rt worden war.
