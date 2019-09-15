import pygame as py
import sys,random
import math

screen = py.display.set_mode((800,800))
py.init()
tank_image = py.image.load('realtank.png')
tank_rect = tank_image.get_rect()
color = (0,0,0)

Tank = {
    'tank1' : {
        'image' : tank_image,
        'new_image' : tank_image,
        'rect' : tank_image.get_rect().copy(),
        'center' : (25,25),
        'angle' : 0
    },

    'tank2' : {
        'image' : tank_image,
        'new_image' : tank_image,
        'rect' : tank_image.get_rect().copy(),
        'center' : (750,750),
        'angle' : 0
    }    
}

Tank['tank1']['rect'].center = (25,25)
Tank['tank2']['rect'].center = (750,750)

def rotate_tank(tank, clock):
    tank['angle'] = (tank['angle'] + clock) % 360
    tank['new_image'] = py.transform.rotate(tank_image, tank['angle'])
    tank['rect'] = tank['new_image'].get_rect()
    tank['rect'].center = tank['center']

def translate(tank):
    r = 2
    x,y = tank['center']
    x += r*math.cos(math.radians(tank['angle']))
    y -= r*math.sin(math.radians(tank['angle']))
    tank['center'] = (x,y)
    tank['rect'].center = (x,y)

done = False
while not done:
    screen.fill(color)
    screen.blit(Tank['tank1']['new_image'], Tank['tank1']['rect'])
    screen.blit(Tank['tank2']['new_image'], Tank['tank2']['rect'])
    py.display.update()

    keys_pressed = py.key.get_pressed()
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True
    
    #Rotation
    if keys_pressed[py.K_a]:
        rotate_tank(Tank['tank1'], 1)
    
    if keys_pressed[py.K_d]:
        rotate_tank(Tank['tank1'], -1)
    
    if keys_pressed[py.K_LEFT]:
        rotate_tank(Tank['tank2'], 1)
    
    if keys_pressed[py.K_RIGHT]:
        rotate_tank(Tank['tank2'], -1)
    
    #Translation
    if keys_pressed[py.K_w]:
        translate(Tank['tank1'])
    if keys_pressed[py.K_UP]:
        translate(Tank['tank2'])

