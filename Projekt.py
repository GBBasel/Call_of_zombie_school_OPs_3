from gamegrid import *
from random import randint
import time

nbLifes = 3  #Leben
nbKillKount = 0  #Punkte
F = 0   # Bullet wird entfernt, wenn F < 0 (nach Ende des Spiel kann nicht mehr geschossen werden)
U = 80  # Zombies erste Welle
V = 19  # Zombies zweite Welle
n = 1   # Boss

#Theoretische Umsetzung der Fenstergrösse:
#gamepadX = 1200
#halfgamepadX = (gamepadX / 2) + 50

def KillKount(self):   #Funktion zum Punktezusammenzählen
    global nbKillKount
    nbKillKount += 1
    playTone([("c'h", 10)])  #Matschiges Geräusch

def Lifes(self):   #Funktion zum Lebenabzählen
    global nbLifes
    nbLifes -= 1
    delay(10)


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

        
        
        
class Human(Actor):
    def __init__(self):
        Actor.__init__(self,"sprites/Human.png")
        self.half_size[0] = self.getWidth(0)/5
        self.half_size[1] = self.getHeight(0)/5
    
    half_size = [0,0]  #Mitte der Figur definiert
    
    def getPos(self):   #Eigene Position bestimmen
        return [self.getX(), self.getY()]
    
    def act(self):   
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
        print(len(colliders))
        for idx, obj in enumerate(colliders): #Wenn Zombie getroffen wird
            obj.hide()
            removeActor(self)
            m_collider.remove(obj)
            KillKount(self)


    
    def getPos(self):     #Bestimmt Position
        return [self.getX(), self.getY()]


class Start(Actor):    #Startbildschirm
    def __init__(self):
        Actor.__init__(self, "sprites/start.jpg")
    
    def act(self):      #Die einzige Funktion des Startbildschirms ist es, zu verschwinden
        removeActor(self)
     
    



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


    