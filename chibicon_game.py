from machine import Pin
from neopixel import NeoPixel

def control_macropixel(np,n,color):
    np [n* 2] = color
    np [n*2+1] = color
    np [90-n*2] = color
    np [90-n*2+1] = color
    np.write()
    
def clear_macropixel(np,n):
    np [n* 2] = [0,0,0]
    np [n*2+1] = [0,0,0]
    np [90-n*2] = [0,0,0]
    np [90-n*2+1] = [0,0,0]  
    np.write()

def full_chibicolors(np):
    for i in range(23):
        r = 193+(25./23.*i)
        g = 131-(92./23.*i)
        b = 251-(131./23.*i)
        np [i* 2] = [int(r) ,int(g) ,int(b)]
        np [i*2+1] = [int(r) ,int(g) ,int(b)]
        np [90-i*2] =  [int(r) ,int(g) ,int(b)]
        np [90-i*2+1] = [int(r) ,int(g) ,int(b)]
    np.write()
    
def full_clear(np):
    for i in range(23):
        np [i* 2] = [0,0,0]
        np [i*2+1] = [0,0,0]
        np [90-i*2] =  [0,0,0]
        np [90-i*2+1] = [0,0,0]
    np.write()

def full_gradient(np,from_color, to_color):
    r_diff = from_color[0]-to_color[0]+0.0
    g_diff = from_color[1]-to_color[1]+0.0
    b_diff = from_color[2]-to_color[2]+0.0
    print(r_diff)
    print(g_diff)
    print(b_diff)
    for i in range(23):
        r = from_color[0]-(r_diff/23.*i)
        g = from_color[1]-(g_diff/23.*i)
        b = from_color[2]-(b_diff/23.*i)
        np [i* 2] = [int(r) ,int(g) ,int(b)]
        np [i*2+1] = [int(r) ,int(g) ,int(b)]
        np [90-i*2] =  [int(r) ,int(g) ,int(b)]
        np [90-i*2+1] = [int(r) ,int(g) ,int(b)]
    np.write()
        
gpio = 19
led_pin = Pin(gpio,Pin.OUT)
led_count = 92
np = NeoPixel(led_pin,led_count)

p2 = Pin(18, Pin.IN, Pin.PULL_UP)
p3 = Pin(15, Pin.IN, Pin.PULL_UP)
p4 = Pin(21, Pin.IN, Pin.PULL_UP)
#control_macropixel(np,[255,0,0])
full_clear(np)
from utime import sleep_ms

x=11
prev_p2 = 1
now_p2 = 1
prev_p3 = 1
now_p3 = 1

while True:
    x=11
    full_clear(np)
    while True:
        control_macropixel(np,x,[255,0,0])
        prev_p2 = now_p2
        now_p2 = p2.value()
        prev_p3 = now_p3
        now_p3 = p3.value()
        if now_p2 == 0 and prev_p2 == 1:
            full_clear(np)
            x=x-1
        if now_p3 == 0 and prev_p3 ==1:
            full_clear(np)
            x=x+1
        if x == 0:
            full_clear(np)
            full_chibicolors(np)
            break
        if x==22:
            full_clear(np)
            full_gradient(np, [255,0,0], [0,0,255])
            break
        sleep_ms(5)
    while p4.value() == 1:
        pass
        

