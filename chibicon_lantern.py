from machine import Pin
from neopixel import NeoPixel
from utime import sleep_ms


def rainbow(deg):
    m=1./60.
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
    myColor=[int(R*255) ,int(G*255) ,int(B*255)]
    return myColor
        
def bottle(n,np, color):
    if n > 4:
        return
    np [2*n] = color
    np [2*n+1] = np[2*n] 
    
def lantern(np, color):
    np[14] = color
    np[15] = np[14]
    np[16] = np[14]
    np[17] = np[14]


def crystal(np, color):
    np[10] = color
    np[11] = np[10]
    np[12] = np[10]
    np[13] = np[10]



def chibicolors(n): # n is of 1 to 360
    if n > 180:
        n = 180-(n-180)
    r = 193+(25./180.*n)
    g = 131-(92./180.*n)
    b = 251-(131./180.*n)
    return [int(r) ,int(g) ,int(b)]

def white_brightness(n):
    if n > 180:
        n = 180-(n-180)
    w = 255-(n)
    r = w
    g = w
    b = w
    return [int(r) ,int(g) ,int(b)]   

def iterate_counters(n, step_size):
    if (n+step_size >= 360):
        n=0
    else:
        n=n+step_size
    return n

bottle_color_0 = (100,0,0)
bottle_color_1 = (0,100,0)
bottle_color_2 = (0,0,100)
bottle_color_3 = (100,100,0)
bottle_color_4 = (0,100,100)
crystal_color = (100,0,100)
lantern_color = (100,100,100)

bottle_counter_0 = 0
bottle_counter_1 = 0
bottle_counter_2 = 0
bottle_counter_3 = 0
bottle_counter_4 = 0
crystal_counter  = 50
lantern_counter  = 0


bottle_step_size_0 = 1
bottle_step_size_1 = 1
bottle_step_size_2 = 1
bottle_step_size_3 = 1
bottle_step_size_4 = 1
crystal_step_size  = 3
lantern_step_size  = 2

gpio = 21
led_pin = Pin(gpio,Pin.OUT)
led_count = 18
np = NeoPixel(led_pin,led_count)


while True:
    sleep_ms(100)
    bottle_counter_0 = iterate_counters(bottle_counter_0, bottle_step_size_0)
    bottle_counter_1 = iterate_counters(bottle_counter_1, bottle_step_size_1)
    bottle_counter_2 = iterate_counters(bottle_counter_2, bottle_step_size_2)
    bottle_counter_3 = iterate_counters(bottle_counter_3, bottle_step_size_3)
    bottle_counter_4 = iterate_counters(bottle_counter_4, bottle_step_size_4)
    crystal_counter = iterate_counters(crystal_counter, crystal_step_size)
    lantern_counter = iterate_counters(lantern_counter, lantern_step_size)

    bottle_color_0 = white_brightness(bottle_counter_0)
    print(crystal_color)
    crystal_color = chibicolors(crystal_counter)
    crystal_color = rainbow(lantern_counter)
    lantern_color = chibicolors(lantern_counter)
    bottle(0,np, bottle_color_0)
    bottle(1,np, bottle_color_1)
    bottle(2,np, bottle_color_2)
    bottle(3,np, bottle_color_3)
    bottle(4,np,  bottle_color_4)
    crystal(np, crystal_color)
    lantern(np, lantern_color)
    np.write()
        
