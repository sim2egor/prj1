import curses
import curses
import paho.mqtt.publish as publish

publish.single("paho/test/single", "up", hostname="192.168.1.46")


def up():
    publish.single("paho/test/single", "up", hostname="192.168.1.46")
    print("up")

def backward():
    publish.single("paho/test/single", "backward", hostname="192.168.1.46")
    print("bakward")

def left():
    publish.single("paho/test/single", "left", hostname="192.168.1.46")
    print("left")

def right():
    publish.single("paho/test/single", "right", hostname="192.168.1.46")
    print("right")

actions = {
    curses.KEY_UP:    up,
    curses.KEY_DOWN:  backward,
    curses.KEY_LEFT:  left,
    curses.KEY_RIGHT: right
}

def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY PRESSED
            curses.halfdelay(3)
            print(key)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY RELEASED
            publish.single("paho/test/single", "stop", hostname="192.168.1.46")
            print('stop()')

curses.wrapper(main)