import side
import tkinter as tk
import mouse 

screen_width = tk.Tk().winfo_screenwidth()
screen_height = tk.Tk().winfo_screenheight()

p1,p2, t1 = 0,0,0
w = [0,0,0,0,0]
h = [0,0,0,0,0]
def main():
    global p1,p2,t1
    while True: 
        for i in range(len(h)):
            p1,p2,t1 = side.get_finger_pos()
            w[i] = int(p1 * screen_width)
            h[i] = int(p2 * screen_height)

        mouse.move(int(sum(w)/len(w)),int(sum(h)/len(h)), duration=0.00001)
        if side.is_clicked(p1, t1):
            mouse.click()
     
if __name__ == '__main__':
    main()
