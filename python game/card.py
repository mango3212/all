import random
import socket   
import time
from colorama import Fore, Back, Style   

#made by lotem
user_ip = socket.gethostbyname(socket.gethostname())   




realG= ["✪","✦","✧"]
numG = [  
    #0
    [
        [random.choice(realG),random.choice(realG),random.choice(realG),random.choice(realG),random.choice(realG)],
        [random.choice(realG),random.choice(realG),random.choice(realG),random.choice(realG),random.choice(realG)],
        [random.choice(realG),random.choice(realG),random.choice(realG),random.choice(realG),random.choice(realG)],
        [random.choice(realG),random.choice(realG),random.choice(realG),random.choice(realG),random.choice(realG)],
        [random.choice(realG),random.choice(realG),random.choice(realG),random.choice(realG),random.choice(realG)],
    ],
    #1
    [
        ["0","1","2","3","4"],
        ["5","6","7","8","9"],
        ["10","11","12","13","14"],
        ["15","16","17","18","19"],
        ["20","21","22","23","24"],
    ]
]


def numg(user, i = 0):
    
    

    try:
        user = int(user)
        while i < 25:
            if user != i:
                i+=1
            elif user == i:
                if i >= 0 and i <= 4:
                    numG[1][0][i] = numG[0][0][i]
                elif i >= 5 and i <= 9:
                    numG[1][1][i-5] = numG[0][1][i-5]
                elif i >= 10 and i <= 14:
                    numG[1][2][i-10] = numG[0][2][i-10]
                elif i >= 15 and i <= 19:
                    numG[1][3][i-15] = numG[0][3][i-15]
                elif i >= 20 and i <= 24:
                    numG[1][4][i-20] = numG[0][4][i-20]
                break
    except:
        pass
    return str(numG[1])

def main():
    load = 0
    while load != 101:
        print("\r{}%".format(load), end = "")
        load += 1
        time.sleep(0.01)  


    
    print(f"\n{Fore.BLUE}enter one of the 25 numbers and hope for the best.\n(there are three symbol ✪, ✦ and ✧){Style.RESET_ALL}",end = "")
    print("\n===========================\n",end = "")
    print("{}".format(str(numG[1]).replace('],', ']\n'),end = '\n'))


    
    while numG[1] != numG[0]: 
        userinput = input(f"{user_ip} =>")
        print("{}".format(numg(userinput).replace("],","]\n")))
    

if __name__ == '__main__':
    main()