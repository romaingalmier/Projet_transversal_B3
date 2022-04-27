# Ecrit ton programme ici ;-)


import serial
from pynput import keyboard
from time import sleep
from pynput.keyboard import Key, Controller


#TEST pour se connecter directement au Serializer et faire avancer le Robot
fin = False
def right():
    return"mogo 1:10 2:40\r"
def left():
    return "mogo 1:40 2:10\r"
def strait():
    return "mogo 1:40 2:40\r"
def back():
    return "mogo 1:-20 2:-20\r"
def stop():
    return "stop\r"

def on_press(key):
    if hasattr(key, 'char'):
        if key.char == 'z':
            print('Rotation Haut')    
            order = 'B'
            ser.write(order.encode())
        if key.char == 's':
            order = 'H'
            ser.write(order.encode())
            print('Rotation Bas')
        if key.char == 'q':
            order = 'E'
            ser.write(order.encode())
            print('Rotation Droite')
        if key.char == 'd':
            order = 'Q'
            ser.write(order.encode())
            print('Rotation Gauche')

    if key == keyboard.Key.esc:
    #key.char == 'a':
        order = 'S'
        ser.write(order.encode())
        print('message_sent')
    if key == keyboard.Key.enter:
    #key.char == 'a':
        order = 'O'
        ser.write(order.encode())
        print('allumer')
    if key == keyboard.Key.left:
    #key.char == 'a':
        order = 'G'
        ser.write(order.encode())
        print('left_key')
    if key == keyboard.Key.right:
        order = 'D'
        ser.write(order.encode())
        print('right_key')
    if key == keyboard.Key.up:
        order = 'A'
        ser.write(order.encode())
        print('strait_key')
    if key == keyboard.Key.down:
        order = 'R'
        ser.write(order.encode())
        print('back_key')
    #if key == keyboard.Key.esc:
     #   quit()


def on_release(key):
    if hasattr(key, 'char'):
        print('char')
    elif key == keyboard.Key.enter:
        order = 'N'
        ser.write(order.encode())
        print("eteindre")
        
        
    else:
        order = 'S'
        print("ok")
        ser.write(order.encode())   
ser = serial.Serial("/dev/ttyUSB0", baudrate = 19200)
sleep(1)
listener = keyboard.Listener(on_press=on_press,on_release=on_release)
kb = Controller()
listener.start()
while True :
    #order = 'E'
    #ser.write(order.encode())
    #order = 'A'
    #ser.write(order.encode())
    print('avancer')
    sleep(0.05)
    #order = 'S'
    #ser.write(order.encode())
#print("stop")

    




# ...or, in a non-blocking fashion: