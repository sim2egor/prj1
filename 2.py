import msvcrt


def up():
    print("up")


def backward():
    print("bakward")


def left():
    print("left")


def right():
    print("right")


keys = {
    0x48: up,
    0x50: backward,
    0x4b: left,
    0x4d: right,
}


def main():
    next_key = None
    while True:
        prefix = ord(msvcrt.getch())
        if prefix == 0xe0:
        # arrow keys
            keycode = ord(msvcrt.getch())
            action = keys.get(keycode, 'unexpected')
            if action is not None:
                action()
            next_key = keycode
            while next_key == keycode:
                next_key = msvcrt.getch()
            # KEY RELEASED
            print('stop()')

if __name__ == '__main__':
    main()
