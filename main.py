import pgzrun
from random import randint
from time import time

WIDTH =  800
HEIGHT = 600

sat = []
lines = []
next_sat = 0

start_time = 0
total_time = 0
end_time = 0

num_sat = 8

def create_satellites():
    global start_time
    for count in range(0, num_sat):
        satellite = Actor('satellite')
        satellite.pos = randint(40,WIDTH-40) , randint(40,HEIGHT-40)
        sat.append(satellite)
    start_time = time()


def draw():
    global total_time
    screen.blit('background for sat', (0,0))
    number = 1
    for satellite in sat:
        screen.draw.text(str(number), (satellite.pos[0], satellite.pos[1]+20))
        satellite.draw()
        number = number +1
        
    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_sat< num_sat:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)

def update():
    pass

def on_mouse_down(pos):
    global next_sat, lines
    if next_sat<num_sat:
        if sat[next_sat].collidepoint(pos):
            if next_sat:
                lines.append(sat[next_sat-1].pos, sat[next_sat].pos)
            next_sat = next_sat+1
        else:
            lines = []
            next_sat = 0

create_satellites()

pgzrun.go()