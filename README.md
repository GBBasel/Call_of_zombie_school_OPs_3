# Call_of_Zombie_school_OPs_3

## 1. Grundstruktur des Spiels:

Die Erde wird von einer andauernden Seuche bedroht. Die Infizierten verlieren ihr Bewusstsein und allen Willen. Es gibt nur noch eins: Jemanden beissen und den Keim übertragen!
Doch nicht alle Menschen ergeben sich so einfach. Ein paar mutige Helden haben sich bewaffnet und es sich zum Ziel gemacht, die Erde zu retten.

Die Hauptidee ist simpel: Auf der einen Seite steht zu Anfang die Hauptfigur, auf der anderen strömen die Zombies heran. Die Hauptfigur kann sich in vier Richtungen bewegen, gesteuert durch die Pfeiltasten, und schiessen, mit Hilfe der Spacetaste. Sobald geschossen wird, erscheint eine Kugel. Wenn diese einen Zombie trifft, verschwinden beide, ausserdem wird ein Punkt hinzugezählt. Die Maximalpunktzahl beträgt 100. Wenn ein Zombie aber den Menschen berührt, dann wird er selbst zum Zombie und das Spiel ist vorbei. Dazu spielt eine nervige 8-bit-Melodie.

![Startbildschirm](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/start.jpg)
Startbildschirm mit Erklärungen zum Spielablauf

## 2. Programmieren:

Zunächst haben wir die Actors definiert. Es gibt einen Menschen (human), die Zombies (zombie) und eine Kugel (bullet). Ausserdem gibt es eine Klasse für den Startbildschirm (start) und eine Klasse, die die Kollissionen überwacht. So lange das Fenster geöffnet ist, werden Punkte zusammengezählt und Leben abgezogen.

### 2.1 Human

![Human](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/Human.png)

Er erscheint zu Beginn des Spiels an der linken Seite des Spielfelds. Mit den vier Pfeiltasten lässt er sich bewegen, wobei er sich immer fünf Pixel bewegt. Sobald er sich aus dem Spielfeld heraus bewegt, wird er an den Rand zurückgesetzt. Somit wird verhindert, dass er das Spielfeld verlässt.

### 2.2 Bullet

![Bullet](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/Bullet.png)

Die Kugel wird durch die Spacetaste erzeugt und  entsteht immer dort, wo sich der Mensch gerade befindet. Sie fragt beim erzeugen die Koordinaten des Human ab. Es gibt eine Verzögerung von dreissig Millisekunden zwischen den Schüssen, damit mit einem Drücken der Taste nicht mehrere Zombies vernichtet werden können.

### 2.3 Zombies

![Zombie](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/Zombie.png)

Die Zombies werden ausserhalb des Spielfeldes an zufälligen Orten erzeugt und gehen nach links. Wenn sie den Menschen berühren, ist das Spiel vorbei.


![Boss](https://raw.githubusercontent.com/GBBasel/Call_of_zombie_school_OPs_3/master/sprites/boss.png)

Der Boss ist der letzte Zombie, der erscheint. Er ist eine Art mutierte Wassermelone. Er lässt sich so wie die anderen Zombies vernichten.





## 3. Schwierigkeiten

Beim Programmieren des Spiel stiessen wir auf verschiedene Schwierigkeiten.

* Zunächst einmal funktionierten die Collissionevents nicht so, wie uns das durch die Tigerjythonseite erklärt worden war. Wir mussten eine andere Methode verwenden, um zum Ziel zu kommen.

* Die Bullet brauchte einen Timer, damit nicht mehr wie eine Kugel auf einmal abgefeuert werden kann.

* Die Titelmelodie musste so angepasst werden, dass sie irgendwann aufhört.

* Das Laggen konnte durch einen print-Befehl gelöst werden. Wir wissen nicht, wieso.

* Die Collissionboxes brauchten eine spezielle Konstruktion.

* Der Mensch konnte zunächst das Spielfeld verlassen, das konnte aber durch einen Befehlsblock geregelt werden.

* Der Startbildschrim brauchte einiges an Kreativität, einen neuen Actor und eine Verzögerung _delay()_.



## 4. Der Code

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
Es werden Variablen für verschiedene Funktionen definiert. Sie steuern das Punktesystem, die Zombiewellen und die Anzahl der Zombies und sollen verhindern, das nach Ende des Spiels noch geschossen werden kann.

```python
def KillKount(self):   #Funktion zum Punktezusammenzählen
    global nbKillKount
    nbKillKount += 1
    playTone([("c'h", 10)])  #Matschiges Geräusch

def Lifes(self):   #Funktion zum Lebenabzählen
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
    
    def check(self, p_obj):   #Collide Überwachung
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
Diese Klasse überwacht die Kollissionsevents. 

```python
class Zombie(Actor):
    def __init__(self, path):
        Actor.__init__(self, path)
        self.half_size[0] = self.getWidth(0)/5
        self.half_size[1] = self.getHeight(0)/5
        
    half_size = [0,0]  #Mitte der Figur definiert
    
    def act(self):   #Bewegen mit zufälliger Geschwindigkeit
        Z = randint(2, 5)
        self.move(Z)
    
    def getPos(self):   #Eigene Position bestimmen
        return [self.getX(), self.getY()]      
```
Dies ist die Klasse der Zombies. Sie bewegen sich mit zufälliger Geschwindigkeit und können ihre Position selbst ermitteln. Kollissionboxen sind hier auch definiert.

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
            self.setX(50)        #Verhindert, das Figur das Spielfeld verlässt
        if self.getY() > 450:
            self.setY(450)
        if self.getY() < 150:
            self.setY(150) 
        colliders = m_collider.check(self)
        for idx, obj in enumerate(colliders):    #Wenn es einen Collide-Event gibt, wird ein Leben abgezogen
            Lifes(self)
```
Dies ist die Klasse des Menschen. Der Mensch hat auch eine Kollissionsbox, Er kann auch die eigene Position bestimmen und es ist ihm unmöglich, die Strasse zu verlassen. Wenn er berührt wird, wird ihm ein Leben abgezogen.

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
Dies ist die Klasse der Bullets. Auch diese haben eine Kollissionsbox. Wenn sie einen Zombie trifft, löst sie aus, dass dieser entfernt wird. Ausserdem verschwindet sie selbst und ein Punkt wird hinzugezählt. Die Variable F verhindert das schiessen nach Beendigung des Spiels.

```python
class Start(Actor):    #Startbildschirm
    def __init__(self):
        Actor.__init__(self, "sprites/start.jpg")
    
    def act(self):      #Die einzige Funktion des Startbildschirms ist es, zu verschwinden
        removeActor(self)
```
Der Actor Start ist der Startbildschirm. Er kann nichts, ausser sich selbst zu entfernen. Damit man ihn überhaupt sieht, werden alle Actors geladen, bevor es eine Verzögerung von drei Sekunden gibt.

```python
def initZombies():
    for i in range(U):       #Erste Welle
        zombie = Zombie("sprites/zombie.png")
        Y = randint(150, 450)
        X = randint(800, 2000)
        addActor(zombie, Location(X, Y), 180)
        m_collider.add(zombie)
    for i in range(V):      #Zweite Welle
        zombie = Zombie("sprites/zombie.png")
        Y = randint(150, 450)
        X = randint(2000, 2200)
        addActor(zombie, Location(X, Y), 180)
        m_collider.add(zombie)
    for i in range(n):      #Boss
        zombie = Zombie("sprites/boss.png")
        Y = randint(150, 450)
        X = 2200
        addActor(zombie, Location(X, Y), 180)
        m_collider.add(zombie)
    doPause()
```
Hier wird definiert, wie die Zombies initialisiert werden sollen. Es gibt zwei Wellen, die unterschiedlich viele Zombies in einer unterschiedlichen Dichte beinhalten. Zuletzt wird der Boss initialisiert, welcher ganz am Schluss geht. Er hat ein anderes Bild als die anderen. Alle Zombies werden so positioniert, dass sie sich auf der Strasse befinden. Sie entstehen auch alle zu Beginn, jedoch kann man sie noch nicht sehen, da sie sich ausserhalb des Spielfeldes befinden.

```python
bullet_timer = time.time()    #Verzögerung Bullet
bullet_time = 0.3         
    
def onKeyRepeated(keyCode):
    global bullet_timer
    if keyCode == 37: # left
        human.setX(human.getX() - 5)
    elif keyCode == 38: # up
        human.setY(human.getY() - 5)
    elif keyCode == 39: # right
        human.setX(human.getX() + 5)      #Steuerung Human durch Pfeiltasten
    elif keyCode == 40: # down
        human.setY(human.getY() + 5)
    elif keyCode == 32:#shoot
        delta = time.time()-bullet_timer   #Mit Space wird gefeuert, Bullet wird mit Timer verzögert
        if delta >= bullet_time:
            bullet_timer = time.time()
            bullet = Bullet()
            addActor(bullet, Location(human.getX() + 25, human.getY() - 12), 0)
```
Mit Hilfe der Pfeiltasten und diesem Funktionsblock kann die Figur gesteuert werden. Immer wenn gedrückt wird, bewegt er sich um fünf Pixel. Wenn mit der Spacetaste gefeuert wird, wird eine Kugel geschossen. Danach verhindert der Timer, das in den nächsten 0,3 Sekunden eine weitere Kugel geschossen werden kann.

```python
makeGameGrid(800, 600, 1, None, "sprites/street.jpg", False, keyRepeated = onKeyRepeated)  #Gamegrid wird erzeugt
setSimulationPeriod(75)   #Spielgeschwindigkeit
initZombies()  #Zombies werden erschaffen
human = Human() #Human wird initialisiert
addActor(human, Location(0, 300), 0)  #Mensch erhält Anfangsposition
start = Start()  #Der Startbildschirm wird initialisiert
addActor(start, Location(400, 300))  #Start erhält Anfangsposition
show()   #Alles wird angezeigt
delay(3000)   #Es gibt eine Verzögerung um drei Sekunden, damit man den Startbildschirm sieht
doRun()   #Beginn der Simulation
playTone([("cdfcdfhedeedcdefdefc'feffecdfcdfhedeedcdefdefc'feffecdfcdfhedeedcdefdefc'feffecdfcdfhedeedcdefdefc'feffecdfcdfhedeedcdefdefc'feffecdfcdfhedeedcdefdefc'feffeccdfcdfhedeedcdefdefc'feffeccdfcdfhedeedcdefdefc'feffec", 200)], block = False)
#Soundtrack
```
Dieser Codeblock initialisiert das Spielfeld, eine Strasse und ermöglicht die Benutzung der Tasten. Die Simulationsperiode wird auf 75 Millisekunden gesetzt. Die Zombies werden initialisiert, so auch der Mensch, der eine Anfangsposition erhält. Der Startbildschirm erscheint und erhält eine Position. Alles wird angezeigt und die Simulation um drei Sekunden verzögert. Das Spiel beginnt und der Soundtrack wird abgespielt.

```python
while not isDisposed():
    setTitle(" KillKount " + str(nbKillKount))  #Anzeige über den Punktestand
    if nbLifes < 0:  # game over
        removeAllActors()
        addActor(Actor("sprites/gameover.gif"), Location(400, 300))
        F =- 1  # Für Bullet
        playTone([("h'f'd'c'", 100)])
    if nbKillKount == U + V + n: #win
        removeAllActors()
        addActor(Actor("sprites/win.png"), Location(400, 300))
        F =- 1   # Für Bullet
        playTone([("c'd'f'h'", 100)])
    delay(50)
```
Diese Schleife überwacht das Spiel, solange das Fenster nicht geschlossen ist. Eine Anzeige mit dem Punktestand wird erzeugt. Wenn die globale Variable nbLifes kleiner als null ist, also alle Leben verbraucht wurden, werden alle Actors entfernt und eine Schrift (_game over_) erscheint. F wird um eins verkleinert, hat daher einen Wert unter null und verhindert so, dass neue Kugel erzeugt werden können. Eine Melodie wird abgespielt.
Wenn die globale Variable nbKillKount gleich viel beträgt wie die Anzahl der Zombies der ersten und der zweiten Welle, sowie die Anzahl der Bosse, dann hat man gewonnen. Die Actors werden entfernt; eine Schrift (_you win_) angezeigt. F verhindert wiederum, dass noch geschossen werden kann. Eine andere Melodie wird gespielt.

