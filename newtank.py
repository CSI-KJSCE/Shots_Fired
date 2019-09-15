import pygame as py
import sys,random
import math

screen = py.display.set_mode((800,800))
py.init()
tank_image = py.image.load('realtank.png')
obstacle_image = py.image.load('rock.png')
bullet_image = py.image.load('missile.png')

tank_rect = tank_image.get_rect()
color = (0,0,0)

Tank = {
    'tank1' : {
        'image' : tank_image,
        'new_image' : tank_image,
        'rect' : tank_image.get_rect().copy(),
        'center' : (25,25),
        'angle' : 0,
        'bullet' : {
            'image' : bullet_image,
            'rect' : bullet_image.get_rect()
        }
    },

    'tank2' : {
        'image' : tank_image,
        'new_image' : tank_image,
        'rect' : tank_image.get_rect().copy(),
        'center' : (750,750),
        'angle' : 0,
        'bullet' : {
            'image' : bullet_image,
            'rect' : bullet_image.get_rect()
        }
    }    
}

Tank['tank1']['rect'].center = (25,25)
Tank['tank2']['rect'].center = (750,750)
obstacles = [(random.randint(40,750),random.randint(40,750)) for i in range(30)]

def draw():
    screen.fill(color)
    draw_obstacles()
    screen.blit(Tank['tank1']['new_image'], Tank['tank1']['rect'])
    screen.blit(Tank['tank2']['new_image'], Tank['tank2']['rect'])
    py.display.update()

def draw_obstacles():
    for i,j in obstacles:
        screen.blit(obstacle_image, (i,j))

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

def bullet_translate(bullet, tank):
    bullet['rect'].center = tank['center']
    x,y = bullet['rect'].center
    r = 7
    while 0 < x < 800 and 0 < y < 800:
        x += r*math.cos(math.radians(tank['angle']))
        y -= r*math.sin(math.radians(tank['angle']))
        bullet['rect'].center = (x,y)
        draw()
        screen.blit(bullet['image'], bullet['rect'])
        py.display.update()

done = False
while not done:
    draw()
    shots_fired1, shots_fired2 = False, False
    keys_pressed = py.key.get_pressed()
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()
            done = True

        if event.type == py.KEYDOWN:
            shots_fired1 = event.key == py.K_e
            shots_fired2 = event.key == py.K_RSHIFT
            
    # print('Shots fired? begin',keys_pressed[py.K_e])
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
    
    #bullet-fire
    if shots_fired1:
        bullet_translate(Tank['tank1']['bullet'], Tank['tank1'])
    if shots_fired2:
        bullet_translate(Tank['tank2']['bullet'], Tank['tank2'])

    # print('Shots fired? end',keys_pressed[py.K_e])
