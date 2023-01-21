import random
USER_X = int(input('km_X---->'))
USER_Y= int(input('km_Y---->'))
S = USER_X*USER_Y
BASE_CORD = [int(USER_Y/2), int(USER_X/2)]
how_mach_gas_need = 5*USER_X
skip = False

boron = input("you want bot or user (Y/n)").lower()
ui ='''
Navigation keys:
N for North
S for South
E for East
W for West

'''
lose = '''

                                    $$\                               
                                    $$ |                              
$$\   $$\  $$$$$$\  $$\   $$\       $$ | $$$$$$\   $$$$$$$\  $$$$$$\  
$$ |  $$ |$$  __$$\ $$ |  $$ |      $$ |$$  __$$\ $$  _____|$$  __$$\ 
$$ |  $$ |$$ /  $$ |$$ |  $$ |      $$ |$$ /  $$ |\$$$$$$\  $$$$$$$$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |$$ |  $$ | \____$$\ $$   ____|
\$$$$$$$ |\$$$$$$  |\$$$$$$  |      $$ |\$$$$$$  |$$$$$$$  |\$$$$$$$\ 
 \____$$ | \______/  \______/       \__| \______/ \_______/  \_______|
$$\   $$ |                                                            
\$$$$$$  |                                                            
 \______/                                                             
'''

won = '''

 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |     ____     | || | _____  _____ | || |              | || | _____  _____ | || |     ____     | || | ____  _____  | |
| | |_  _||_  _| | || |   .'    `.   | || ||_   _||_   _|| || |              | || ||_   _||_   _|| || |   .'    `.   | || ||_   \|_   _| | |
| |   \ \  / /   | || |  /  .--.  \  | || |  | |    | |  | || |              | || |  | | /\ | |  | || |  /  .--.  \  | || |  |   \ | |   | |
| |    \ \/ /    | || |  | |    | |  | || |  | '    ' |  | || |              | || |  | |/  \| |  | || |  | |    | |  | || |  | |\ \| |   | |
| |    _|  |_    | || |  \  `--'  /  | || |   \ `--' /   | || |              | || |  |   /\   |  | || |  \  `--'  /  | || | _| |_\   |_  | |
| |   |______|   | || |   `.____.'   | || |    `.__.'    | || |   _______    | || |  |__/  \__|  | || |   `.____.'   | || ||_____|\____| | |
| |              | || |              | || |              | || |  |_______|   | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
'''


if boron == 'n':
    Targets_count = int(input('targets count    :'))
    GasForFly = int(input('gas for fly      :'))

    print(f'you have {USER_X}km .you need to bomb {Targets_count} targets.min fuel is {how_mach_gas_need} liters.the amount of fuel you get is {GasForFly} liters.\n{ui}')
    while Targets_count !=0:
        print(f'you in cord {BASE_CORD}. fuel = {GasForFly}. your S in ({USER_X},{USER_Y})')
        target_cord = input('target cord x,y for example 15,60.\n_______________________:')
        targetY = int(target_cord.split(',')[1])
        targetX = int(target_cord.split(',')[0])
        dist = (((BASE_CORD[0]-targetX)**2)+((BASE_CORD[1]-targetY)**2)) ** (1/2) 
        if targetX > USER_X or targetY > USER_Y:
            print("target not inside the cord")
            skip = True
        print(f'target cord is ({targetX},{targetY})')
        if skip == False:
            if BASE_CORD[1] < targetY:
                h = 'N'
            elif BASE_CORD[1] > targetY:
                h = 'S'
            else:
                h = "dont move on y"
            if BASE_CORD[0] < targetX:
                hx = 'E'
            elif BASE_CORD[0] > targetX:
                hx = 'W'
            else:
                hx = "dont move on x"
            helpornot = input("you what to know were to go(feul-3 by say yes).(Y/n)\n________________________________________________________________#").lower()
            if helpornot == 'y':
                print(f"dist = {dist},move to :{h} {hx}")
                GasForFly-=3


            were_u_what_togo = input("|N, NE, NW, S, SE, SW, E, W\n________________________#").lower()
            match were_u_what_togo:
                case "n": 
                    BASE_CORD[1]+=1
                    GasForFly -= 5
                case "ne": 
                    BASE_CORD[1]+=1
                    BASE_CORD[0]+=1
                    GasForFly -= 5
                case "en": 
                    BASE_CORD[1]+=1
                    BASE_CORD[0]+=1
                    GasForFly -= 5
                case "e": 
                    BASE_CORD[0]+=1
                    GasForFly -= 5
                case "es": 
                    BASE_CORD[1]-=1
                    BASE_CORD[0]+1
                    GasForFly -= 5
                case "se": 
                    BASE_CORD[1]-=1
                    BASE_CORD[0]+1
                    GasForFly -= 5
                case "s": 
                    BASE_CORD[1]-=1
                    GasForFly -= 5
                case "sw": 
                    BASE_CORD[1]-=1
                    BASE_CORD[0]-=1
                    GasForFly -= 5
                case "ws": 
                    BASE_CORD[1]-=1
                    BASE_CORD[0]-=1
                    GasForFly -= 5
                case "w": 
                    BASE_CORD[0]-=1
                    GasForFly -= 5
                case "wn":
                    BASE_CORD[0]-=1
                    BASE_CORD[1]+=1
                    GasForFly -= 5
                case "nw":
                    BASE_CORD[0]-=1
                    BASE_CORD[1]+=1
                    GasForFly -= 5
            if [targetX, targetY] == BASE_CORD:
                print("target has been eliminated :)")
                Targets_count-=1
        if GasForFly <= 0:
            print(lose)
            exit()
    print(won)
#############################################################################################################################
else:
    Targets_count = random.randint(0,int(USER_X/2))
    GasForFly = random.randint(0,int((USER_X*5)+10))
    print(f'you have {USER_X}km .you need to bomb {Targets_count} targets.min fuel is {how_mach_gas_need} liters.the amount of fuel you get is {GasForFly} liters.\n{ui}')
    while Targets_count !=0:
        print(f'you in cord {BASE_CORD}. fuel = {GasForFly}. your S in ({USER_X},{USER_Y})')
        target_cord = f'{random.randint(0,USER_X)},{random.randint(0,USER_Y)}'
        targetY = int(target_cord.split(',')[1])
        targetX = int(target_cord.split(',')[0])
        dist = (((BASE_CORD[0]-targetX)**2)+((BASE_CORD[1]-targetY)**2)) ** (1/2) 
        print(f'target cord is ({targetX},{targetY})')
        if skip == False:
            if BASE_CORD[1] < targetY:
                h = 'N'
            elif BASE_CORD[1] > targetY:
                h = 'S'
            else:
                h = "dont move on y"
            if BASE_CORD[0] < targetX:
                hx = 'E'
            elif BASE_CORD[0] > targetX:
                hx = 'W'
            else:
                hx = "dont move on x"
            helpornot = input("you what to know were to go(feul-3 by say yes).(Y/n)\n________________________________________________________________#").lower()
            if helpornot == 'y':
                print(f"dist = {dist},move to :{h} {hx}")
                GasForFly-=3


            were_u_what_togo = input("|N, NE, NW, S, SE, SW, E, W\n________________________#").lower()
            match were_u_what_togo:
                case "n": 
                    BASE_CORD[1]+=1
                    GasForFly -= 5
                case "ne": 
                    BASE_CORD[1]+=1
                    BASE_CORD[0]+=1
                    GasForFly -= 5
                case "en": 
                    BASE_CORD[1]+=1
                    BASE_CORD[0]+=1
                    GasForFly -= 5
                case "e": 
                    BASE_CORD[0]+=1
                    GasForFly -= 5
                case "es": 
                    BASE_CORD[1]-=1
                    BASE_CORD[0]+1
                    GasForFly -= 5
                case "se": 
                    BASE_CORD[1]-=1
                    BASE_CORD[0]+1
                    GasForFly -= 5
                case "s": 
                    BASE_CORD[1]-=1
                    GasForFly -= 5
                case "sw": 
                    BASE_CORD[1]-=1
                    BASE_CORD[0]-=1
                    GasForFly -= 5
                case "ws": 
                    BASE_CORD[1]-=1
                    BASE_CORD[0]-=1
                    GasForFly -= 5
                case "w": 
                    BASE_CORD[0]-=1
                    GasForFly -= 5
                case "wn":
                    BASE_CORD[0]-=1
                    BASE_CORD[1]+=1
                    GasForFly -= 5
                case "nw":
                    BASE_CORD[0]-=1
                    BASE_CORD[1]+=1
                    GasForFly -= 5
            if [targetX, targetY] == BASE_CORD:
                print("target has been eliminated :)")
                Targets_count-=1
        if GasForFly <= 0:
            print(lose)
            exit()
    print(won)