from gamegrid import *
from random import randint


NbLifes = 3
nbKillKount = 0

def KillKount(self):
        global nbKillKount
        nbKillKount += 1
        playTone([("c''g'a'f'", 100)])


class collider:
    objects = []
    def add(self, obj):
        self.objects.append(obj)
        return
    
    def remove(self, obj):
        self.objects.remove(obj)
    
    def check(self, p_obj):
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
        self.half_size[0] = self.getWidth(0)/2
        self.half_size[1] = self.getHeight(0)/2
        
    half_size = [0,0]
    
    def act(self):
        self.move(1)
    
    def getPos(self):
        return [self.getX(), self.getY()]

        
        
        
class Human(Actor):
    def __init__(self):
        Actor.__init__(self,"sprites/guywithgun.gif")
        self.half_size[0] = self.getWidth(0)/2
        self.half_size[1] = self.getHeight(0)/2
    
    half_size = [0,0]
    def getPos(self):
        return [self.getX(), self.getY()]
    
    def act(self):
        if self.getX() > 650:
            self.setX(650)
        if self.getX() < 150:
            self.setX(150)
        if self.getY() > 450:
            self.setY(450)
        if self.getY() < 150:
            self.setY(150)
        
class Bullet(Actor):
    def __init__(self):
        Actor.__init__(self, "sprites/Orb.gif")
        self.half_size[0] = self.getWidth(0)/2
        self.half_size[1] = self.getHeight(0)/2
    
    half_size = [0,0]
        
        
    def act(self):
        self.move(25)
        colliders = m_collider.check(self)
        print(len(colliders))
        for idx, obj in enumerate(colliders):
            obj.hide()
            removeActor(self)
            m_collider.remove(obj)
            KillKount(self)

    
    def getPos(self):
        return [self.getX(), self.getY()]
       
            
    



def initZombies():   
    for i in range(3):
        zombie = Zombie("sprites/zombie" + str(i) + ".jpg")
        Y = randint(0, 600)
        addActor(zombie, Location(800, Y), 180)
        m_collider.add(zombie)
    doPause()


            
    
def onKeyRepeated(keyCode):
    if keyCode == 37: # left
        human.setX(human.getX() - 5)
    elif keyCode == 38: # up
        human.setY(human.getY() - 5)
    elif keyCode == 39: # right
        human.setX(human.getX() + 5)
    elif keyCode == 40: # down
        human.setY(human.getY() + 5)
    elif keyCode == 32:#shoot
        bullet = Bullet()
        addActor(bullet, Location(human.getX(), human.getY()), 0)



            
        
makeGameGrid(800, 600, 1, None, "sprites/lane.gif", False, keyRepeated = onKeyRepeated)
setSimulationPeriod(50)
initZombies()
human = Human()
addActor(human, Location(0, 300), 0)
show()
doRun()



while not isDisposed():
    setTitle(" #KillKount " + str(nbKillKount))
    if NbLifes == 0:  # game over
        addActor(Actor("sprites/gameover.gif"), Location(400, 285))
        removeActor(Human)
        doPause()
    delay(100)
    