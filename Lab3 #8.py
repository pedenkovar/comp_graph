'''import matplotlib.pyplot as plt
x = []
y = []

for line in open('DS8.txt', 'r'):
    lines = [i for i in line.split()]
    x.append(960-int(lines[1]))
    y.append(int(lines[0]))


plt.figure(figsize=(8, 8))    
plt.scatter(x, y, marker = 'o', c = 'b', s = 2) 

plt.gca()
plt.axis('off')

plt.savefig('affine transformation.png', dpi = 120)
'''

from tkinter import *
from pyautogui import screenshot
from math import pi, cos, sin
def rotate(x, y, teta, center=480):
    ang = (pi/180)*teta
 
    x -= center
    y -= center

    x = x*cos(ang)-y*sin(ang)
    y = y*cos(ang)+x*sin(ang)

    x += center
    y += center

    canvas.create_line(x,y,x+1,y+1, fill="blue")

window_width = 960
window_height = 960

window = Tk()
window.title("Лабораторна робота №3: Афінне перетворення")

canvas = Canvas(window,width=window_width,height=window_height )
w, h = window.winfo_width(), window.winfo_height()
window.geometry("+0+0")
canvas.pack()


file = open("DS8.txt")
for line in file:
    data = line.split(sep=" ")
    x = float(data[0])
    y = float(data[1])
    alpha = 10 * (3 + 1)
    rotate(x, y, alpha)


window.mainloop()
screenshot('screenshot.png', region = (5,30,window_width,window_height+10))