import mouse, threading, time
import screen_brightness_control as screen
def checkMP():
    mousePx, yMP = mouse.get_position()
    time.sleep(0.1)
    x, y = mouse.get_position()
    if yMP != y:
        get = screen.get_brightness()
        
        if yMP > y:
            up = int(screen.get_brightness()[0])
            up +=20
            screen.set_brightness(up)
        else:
            down = int(screen.get_brightness()[0])
            down -=20
            screen.set_brightness(down)
def main():
    while True:
        t = threading.Thread(target=checkMP)
        t.start()
        t.join()
if __name__ == "__main__":
    main()