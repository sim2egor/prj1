import curses
def up():
    print("up")

def backward():
    print("bakward")

def left():
    print("left")

def right():
    print("right")

actions = {
    259:    up,
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
            print('stop()')

curses.wrapper(main)