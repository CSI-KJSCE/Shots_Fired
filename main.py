import pygame as py
import os,sys,random
import numpy as np
import math

screen = py.display.set_mode((800, 800))
tank_rot_1= 0
tank_rot_2= 0

player_x1 = 30
player_y1 = 30

player_x2 = 1570
player_y2 = 1570

curr_x1 = player_x1 + 20
curr_y1 = player_y1

curr_y2 =player_y2
curr_x2 = player_x2 + 20
py.init()
done = False

#array of pairs
randnumsx = np.random.randint(-800, 800, 80)
randnumsy = np.random.randint(-800, 800, 80)
cord = randnumsx+randnumsy
it1 = iter(randnumsx)
it2 = iter(randnumsy)
cord = list(zip(it1,it2))   #array of co ordinates

tank1 = py.image.load('realtank.png')
tank2 = py.image.load('realtank.png')    #image size is 40x40
bullet1 = py.image.load('missile.png')
bullet2 = py.image.load('missile.png')
background = py.image.load('background.jpg')
obstacle = py.image.load('rock.png')

screen = py.display.set_mode((800, 800))
# screen.blit(background,[0,0])

rect1 = tank1.get_rect()
rect2 = tank2.get_rect()
rect1.center = (50,50)
rect2.center =(750,750)

new_image_1 = tank1
new_image_2 = tank2

def draw_obstacles(screen):
    for i,j in cord:
        screen.blit(obstacle, (i, j))



def draw():
    global tank1, tank2,screen,new_image1,new_image2
    screen = py.display.set_mode((800,800))
    # screen.blit(background,[0,0])               #setting the background image
    draw_obstacles(screen)
    screen.blit(new_image_1,rect1)  # setting the tank1 pos
    screen.blit(new_image_2,rect2)
    py.display.flip()  # usded to view the updates on screen as soon as we see them.

def rotate_1(clock):
    global new_image_1,old_center_1,rect1,tank_rot_1,new_image_2,old_center_2,rect2,tank_rot_2
    screen = py.display.set_mode((800, 800))
    draw_obstacles(screen)
    old_center_1 = rect1.center
    tank_rot_1 = (tank_rot_1 + 3) % 360
    new_image_1 = py.transform.rotate(tank1, (clock)*tank_rot_1)
    rect1 = new_image_1.get_rect()
    rect1.center = old_center_1
    screen.blit(new_image_1,rect1)
    screen.blit(new_image_2,rect2)
    py.display.flip()

def rotate_2(clock):
    global new_image_1,old_center_1,rect1,tank_rot_1,new_image_2,old_center_2,rect2,tank_rot_2
    screen = py.display.set_mode((800, 800))
    draw_obstacles(screen)
    old_center_2 = rect2.center
    tank_rot_2 = (tank_rot_2 + 3) % 360
    new_image_2 = py.transform.rotate(tank2,(clock)*tank_rot_2)
    rect2 = new_image_2.get_rect()
    rect2.center = old_center_2
    screen.blit(new_image_2,rect2)
    screen.blit(new_image_1,rect1)
    py.display.flip()

def bullet_1(bullet_x,bullet_y):
    global new_iamge_1,rect1,new_iamge_2,rect2
    screen = py.display.set_mode((800,800))
    draw_obstacles(screen)
    screen.blit(new_image_1, rect1)  # setting the tank1 pos
    screen.blit(new_image_2,rect2)
    screen.blit(bullet1,(bullet_x,bullet_y))
    py.display.flip()

def bullet_2(bullet_x,bullet_y):
    global new_iamge_1, rect1, new_iamge_2, rect2
    screen = py.display.set_mode((800,800))
    draw_obstacles(screen)
    screen.blit(new_image_1, rect1)  # setting the tank1 pos
    screen.blit(new_image_2, rect2)
    screen.blit(bullet2,(bullet_x,bullet_y))
    py.display.flip()


def main():
    global player_x1, player_y1,player_x2, player_y2,curr_y1,curr_y2,curr_x1,curr_x2,tank1,tank2,tank_rot_1,tank_rot_2,rect1,rect2,new_image1,new_image2
    global done
    while not done:

        keys_pressed = py.key.get_pressed()
        for event in py.event.get():
            if event.type == py.QUIT:
                done = True

        #moving the first tank anti-clockwise
        if keys_pressed[py.K_a]:
            rotate_1(1)
            draw()
        # moving the first tank clockwise
        if keys_pressed[py.K_d]:
            rotate_1(-1)
            draw()

        #translation motion for the first tank.
        if keys_pressed[py.K_w]:
            (player_x1,player_y1) = rect1.center
            player_x1 = player_x1 +(player_x1*math.cos(tank_rot_1%90))*0.01
            player_y1 = player_y1 +(player_y1*math.sin(tank_rot_1%90))*0.01
            rect1.center = (player_x1,player_y1)
            draw()

        #moving the second tank anit-clockwise.
        if keys_pressed[py.K_LEFT]:
            rotate_2(1)
            draw()
        #moving the second tank clockwise.
        if keys_pressed[py.K_RIGHT]:
            rotate_2(-1)
            draw()

        # translation motion for the second tank.
        if keys_pressed[py.K_UP]:
            (player_x2, player_y2) = rect2.center
            player_x2 = player_x2 + (player_x2 * math.cos(tank_rot_2 % 90)) * 0.01
            player_y2 = player_y2 + (player_y2 * math.sin(tank_rot_2 % 90)) * 0.01
            rect2.center = (player_x2, player_y2)
            draw()

        py.display.flip()


if __name__ == '__main__':
    main()

