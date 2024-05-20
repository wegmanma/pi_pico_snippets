from machine import Pin
from neopixel import NeoPixel

def getRGB(deg):
    m=1/60
    if deg>=0 and deg<60:
        R=1
        G=0
        B=m*deg
    if deg>=60 and deg<120:
        R=1-m*(deg-60)
        G=0
        B=1
    if deg>=120 and deg<180:
        R=0
        G=m*(deg-120)
        B=1
    if deg>=180 and deg<240:
        R=0
        G=1
        B=1-m*(deg-180)
    if deg>=240 and deg<300:
        R=m*(deg-240)
        G=1
        B=0
    if deg>=300 and deg<360:
        R=1
        G=1-m*(deg-300)
        B=0
    myColor=(R,G,B)
    return myColor
        
def bottle(n,np):
    if n > 4:
        return
    if bottle.iterator[n]+bottle.offset[n] < 360:
    	bottle.iterator[n] += bottle.offset[n]
    else:
    	bottle.iterator[n] = bottle.iterator[n]+bottle.offset[n]-360
    np [2*n] = getRGB(bottle.iterator)
    np [2*n+1] = np[2*n] 
	
def lantern(np):
    if lantern.iterator+lantern.offset < 360:
        lantern.iterator += lantern.offset
    else:
        lantern.iterator = lantern.iterator+lantern.offset-360
    np[14] = getRGB(lantern.iterator)
    np[15] = np[14]
    np[16] = np[14]
    np[17] = np[14]


def crystal(np):
    if crystal.iterator+crystal.offset < 360:
        crystal.iterator += crystal.offset
    else:
        crystal.iterator = crystal.iterator+crystal.offset-360
    np[10] = getRGB(crystal.iterator)
    np[11] = np[10]
    np[12] = np[10]
    np[13] = np[10]


bottle.iterator={0,0,0,0,0}
lantern.iterator=0
crystal.iterator=0
bottle.offset={2,3,3,2,2}
lantern.offset=2
crystal.offset=3


gpio = 21
led_pin = Pin(gpio,Pin.OUT)
led_count = 4
np = NeoPixel(led_pin,led_count)


for i in range(4):
    bottle(0,np)
    bottle(1,np)
    bottle(2,np)
    bottle(3,np)
    bottle(4,np)
    crystal(np)
    lantern(np)
np.write()
        
