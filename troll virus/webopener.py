import webbrowser,random,keyboard,mouse,time,threading

safe = lambda arg: arg.startswith('http://')
mousepose = [mouse.get_position(),mouse.get_position()]


def virus():
    for i in range(len(mousepose)):mousepose[i] = mouse.get_position()
    if mousepose[0] != mousepose[1]:
        with open('c.txt', 'r') as f:
            FULL_FILE = f.readlines()
            urls = list(filter(safe, FULL_FILE))
            webbrowser.open(random.choice(urls))
            time.sleep(0.5)

def main():
    while keyboard.is_pressed(' ') == False:
       V = threading.Thread(target=virus)
       V.start()
       V.join()
       
if __name__ == '__main__':
    main()