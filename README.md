# Call_of_Zombie_school_OPs_3

## Grundstruktur des Spiels:

Die Erde wird von einer andauernden Seuche bedroht. Die Infizierten verlieren ihr Bewusstsein und allen Willen. Es gibt nur noch eins: Jemanden beissen und den Keim �bertragen!
Doch nicht alle Menschen ergeben sich so einfach. Ein paar mutige Helden haben sich bewaffnet und es sich zum Ziel gemacht, die Erde zu retten.

Die Hauptidee ist simpel: Auf der einen Seite steht zu Anfang die Hauptfigur, auf der anderen str�men die Zombies heran. Die Hauptfigur kann sich in vier Richtungen bewegen, gesteuert durch die Pfeiltasten, und schiessen, mit Hilfe der Spacetaste. Sobald geschossen wird, erscheint eine Kugel. Wenn diese einen Zombie trifft, verschwinden beide, ausserdem wird ein Punkt hinzugez�hlt. Die Maximalpunktzahl betr�gt 100. Wenn ein Zombie aber den Menschen ber�hrt, dann wird er selbst zum Zombie und das Spiel ist vorbei. Dazu spielt eine nervige 8-bit-Melodie.

![Startbildschirm](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/start.jpg)
Startbildschirm mit Erkl�rungen zum Spielablauf

## Programmieren:

Zun�chst haben wir die Actors definiert. Es gibt einen Menschen (human), die Zombies (zombie) und eine Kugel (bullet). Ausserdem gibt es eine Klasse f�r den Startbildschirm (start) und eine Klasse, die die Kollissionen �berwacht. So lange das Fenster ge�ffnet ist, werden Punkte zusammengez�hlt und Leben abgezogen.

### Human

![Human](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/Human.png)

Er erscheint zu Beginn des Spiels an der linken Seite des Spielfelds. Mit den vier Pfeiltasten l�sst er sich bewegen, wobei er sich immer f�nf Pixel bewegt. Sobald er sich aus dem Spielfeld heraus bewegt, wird er an den Rand zur�ckgesetzt. Somit wird verhindert, dass er das Spielfeld verl�sst.

### Bullet

![Bullet](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/Bullet.png)

Die Kugel wird durch die Spacetaste erzeugt und  entsteht immer dort, wo sich der Mensch gerade befindet. Sie fragt beim erzeugen die Koordinaten des Human ab. Es gibt eine Verz�gerung von dreissig Millisekunden zwischen den Sch�ssen, damit mit einem Dr�cken der Taste nicht mehrere Zombies vernichtet werden k�nnen.

### Zombies

![Zombie](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/Zombie.png)

Die Zombies werden ausserhalb des Spielfeldes an zuf�lligen Orten erzeugt und gehen nach links. Wenn sie den Menschen ber�hren, ist das Spiel vorbei.


![Boss](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/boss.png)

Der Boss ist der letzte Zombie, der erscheint. Er ist eine Art mutierte Wassermelone. Er l�sst sich so wie die anderen Zombies vernichten.





## Schwierigkeiten

Beim Programmieren des Spiel stiessen wir auf verschiedene Schwierigkeiten.

* Zun�chst einmal funktionierten die Collissionevents nicht so, wie uns das durch die Tigerjythonseite erkl�rt worden war. Wir mussten eine andere Methode verwenden, um zum Ziel zu kommen.

* Die Bullet brauchte einen Timer, damit nicht mehr wie eine Kugel auf einmal abgefeuert werden kann.

* Die Titelmelodie musste so angepasst werden, dass sie irgendwann aufh�rt.

* Das Laggen konnte durch einen print-Befehl gel�st werden. Wir wissen nicht, wieso.

* Die Collissionboxes brauchten eine spezielle Konstruktion.

* Der Mensch konnte zun�chst das Spielfeld verlassen, das konnte aber durch einen Befehlsblock geregelt werden.

* Der Startbildschrim brauchte einiges an Kreativit�t, einen neuen Actor und eine Verz�gerung _delay()_.



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
Es werden Variablen f�r verschiedene Funktionen definiert. Sie steuern das Punktesystem, die Zombiewellen und die Anzahl der Zombies und sollen verhindern, das nach Ende des Spiels noch geschossen werden kann.

```python
def KillKount(self):   #Funktion zum Punktezusammenz�hlen
    global nbKillKount
    nbKillKount += 1
    playTone([("c'h", 10)])  #Matschiges Ger�usch

def Lifes(self):   #Funktion zum Lebenabz�hlen
    global nbLifes
    nbLifes -= 1
    delay(10)
```
Diese globalen Definitionen steuern das Verhalten bei Kollissionen.

```python
class collider:   #Liste aus Objekten
    objects = []
    def add(self, obj):
        self.objects.append(obj)
        return
    
    def remove(self, obj):   #Objekte werden entfernt
        self.objects.remove(obj)
    
    def check(self, p_obj):   #Collide �berwachung
        colliders = []
        p_pos = p_obj.getPos()
        left = p_pos[0]-p_obj.half_size[0]
        right = p_pos[0]+p_obj.half_size[0]
        top = p_pos[1]-p_obj.half_size[1]
        bottom = p_pos[1]+p_obj.half_size[1]
        for idx, obj in enumerate(self.objects):
            obj_pos = obj.getPos()
            left2 = obj_pos[0]-obj.half_size[0]
            right2 = obj_pos[0]+obj.half_size[0]
            top2 = obj_pos[1]-obj.half_size[1]
            bottom2 = obj_pos[1]+obj.half_size[1]
            if left <= right2 and right >= left2 and top <= bottom2 and bottom >= top2:
                colliders.append(obj)
        return colliders

m_collider = collider()
```
Diese Klasse �berwacht die Kollissionsevents. 

```python
class Zombie(Actor):
    def __init__(self, path):
        Actor.__init__(self, path)
        self.half_size[0] = self.getWidth(0)/5
        self.half_size[1] = self.getHeight(0)/5
        
    half_size = [0,0]  #Mitte der Figur definiert
    
    def act(self):   #Bewegen mit zuf�lliger Geschwindigkeit
        Z = randint(2, 5)
        self.move(Z)
    
    def getPos(self):   #Eigene Position bestimmen
        return [self.getX(), self.getY()]      
```
Dies ist die Klasse der Zombies. Sie bewegen sich mit zuf�lliger Geschwindigkeit und k�nnen ihre Position selbst ermitteln. Kollissionboxen sind hier auch definiert.

```python
class Human(Actor):
    def __init__(self):
        Actor.__init__(self,"sprites/Human.png")
        self.half_size[0] = self.getWidth(0)/5
        self.half_size[1] = self.getHeight(0)/5
    
    half_size = [0,0]  #Mitte der Figur definiert
    
    def getPos(self):   #Eigene Position bestimmen
        return [self.getX(), self.getY()]
    
    def act(self):
        print("Yeah")
        if self.getX() > 550:
            self.setX(550)
        if self.getX() < 50:
            self.setX(50)        #Verhindert, das Figur das Spielfeld verl�sst
        if self.getY() > 450:
            self.setY(450)
        if self.getY() < 150:
            self.setY(150) 
        colliders = m_collider.check(self)
        for idx, obj in enumerate(colliders):    #Wenn es einen Collide-Event gibt, wird ein Leben abgezogen
            Lifes(self)
```

Dies ist die Klasse des Menschen. Der Mensch hat auch eine Kollissionsbox, Er kann auch die eigene Position bestimmen und es ist ihm unm�glich, die Strasse zu verlassen. Wenn er ber�hrt wird, wird ihm ein Leben abgezogen.


```python
class Bullet(Actor):
    def __init__(self):
        Actor.__init__(self, "sprites/Bullet.png")
        self.half_size[0] = self.getWidth(0)/5
        self.half_size[1] = self.getHeight(0)/5
    
    half_size = [0,0]
        
        
    def act(self):
        if F < 0:    #Wenn Spiel vorbei, kann nicht mehr geschossen werden
            removeActor(self)
        self.move(25)  #Bewegt sich nach vorne
        colliders = m_collider.check(self)
        for idx, obj in enumerate(colliders): #Wenn Zombie getroffen wird
            removeActor(obj)
            m_collider.remove(obj)
            KillKount(self)
            removeActor(self)

    
    def getPos(self):     #Bestimmt Position
        return [self.getX(), self.getY()]
```
Dies ist die Klasse der Bullet. 
