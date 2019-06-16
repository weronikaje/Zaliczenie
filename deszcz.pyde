class kropla(object):
    def __init__(self):
        self.x=0
        self.y=0
        self.szybkosc=0
    def ruch(self):
        self.y = self.y + self.szybkosc
    def powrot(self):
        if(self.y>500):
            self.y=0
            self.x=random(width)
    def rysuj(self):
        rect(self.x, self.y, 2, 4)
        
def setup():
    global deszcz
    size(600,600)
    frameRate(60)
    deszcz=[]
    for i in range(0,400):
        deszcz.append(kropla())
        deszcz[i].x=random(width)
        deszcz[i].y=random(height)
        deszcz[i].szybkosc=random(8,10)
    rectMode(CENTER)
    noStroke()

def draw():
    background(26, 31, 61)
    fill(13, 61, 18)
    rect(width/2,550,width, 100)
    for i in range(0,400):
        deszcz[i].ruch()
        deszcz[i].powrot()
        fill(18, 171, 255)
        deszcz[i].rysuj()
