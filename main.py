#LIBRARIES AND VARIABLES
############################################################

from tkinter import *
from time import *
from random import*
from math import*

screen_max = 900

tk = Tk()
s = Canvas(tk, width=screen_max,height=screen_max, background="white")
s.pack()

num_parents = 100
parent_size = 8
parent_speed = 14

parent_positions = []
parent_velocities = []

parents = []
lines = []

#set initial position & velocity
for i in range(num_parents):
    parent_positions.append([round(uniform(0,screen_max), 2), round(uniform(0,screen_max), 2)])
    parent_velocities.append([round(uniform(-1,1), 2), round(uniform(-1,1), 2)])

while True:

    #set velocities
    for x,i in enumerate(parent_positions):
        if i[0] >= screen_max or i[0] <= 0:
            parent_velocities[x][0] *= -1

        if i[1] >= screen_max or i[1] <= 0:
            parent_velocities[x][1] *= -1

        i[0] += parent_velocities[x][0]*parent_speed
        i[1] += parent_velocities[x][1]*parent_speed

    #Draw Content
    for i in parent_positions:
        parents.append(s.create_oval(i[0], i[1], i[0]+parent_size,i[1]+parent_size, fill="blue"))

        for x in parent_positions:
            if sqrt((i[0]-x[0])**2+(i[1]-x[1])**2) <= 100:
                lines.append(s.create_line(i[0],i[1],x[0],x[1]))


    s.update()
    tk.after(1)

    #Delete Content
    
    for i in lines:
        s.delete(i)

    for i in parents:
        s.delete(i)