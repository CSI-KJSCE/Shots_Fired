import pygame as py
import os,sys,random
import numpy as np
import math

#Parts to be done
#1.rotation match for bullet and tank. Angle of rotation for both is not matching
#2.Firing of bullets from the rotated tank.
#3.obstacle and tank collision. Stop tank from colliding with obstacles
#4.obstacle and bullet collision.Stop bullets from colliding with obstacles
#5.tank-tank match.Stop the two tanks from colliding
#6.corner case.Tank should not escape the window.


screen = py.display.set_mode((800, 800))
rot_speed = 0.07
tank_rot_1= 0
tank_rot_2= 0

player_x1 = 30
player_y1 = 30

player_x2 = 1570
player_y2 = 1570

# curr_x1 = player_x1 + 20
# curr_y1 = player_y1
#
# curr_y2 =player_y2
# curr_x2 = player_x2 + 20
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
screen.blit(background,[0,0])


rect1 = tank1.get_rect()
rect2 = tank2.get_rect()


def draw_obstacles(screen):
    for i,j in cord:
        screen.blit(obstacle, (i, j))



def draw():
    global tank1, tank2,screen,new_image1,new_image2
    screen = py.display.set_mode((800,800))
    screen.blit(background,[0,0])               #setting the background image
    draw_obstacles(screen)
    screen.blit(new_image1,rect1)  # setting the tank1 pos
    screen.blit(new_image2,rect2)
    py.display.flip()  # used to view the updates on screen as soon as we see them.

# def bullet_1(bullet_x,bullet_y):
#     global tank1, tank2
#     screen = py.display.set_mode((800,800))
#     # screen.blit(background, [0, 0])
#     draw_obstacles(screen)
#     screen.blit(new_image1,rect1)  # setting the tank1 pos
#     screen.blit(new_image2,rect2)
#     screen.blit(bullet1,(bullet_x,bullet_y))
#     py.display.flip()

# def bullet_2(bullet_x,bullet_y):
#     global tank1, tank2
#     screen = py.display.set_mode((800,800))
#     # screen.blit(background, [0, 0])
#     draw_obstacles(screen)
#     screen.blit(tank1, (player_x1, player_y1))  # setting the tank1 pos
#     screen.blit(tank2, (player_x2, player_y2))
#     screen.blit(bullet2,(bullet_x,bullet_y))
#     py.display.flip()


def main():
    global player_x1, player_y1,player_x2, player_y2,curr_y1,curr_y2,curr_x1,curr_x2,tank1,tank2,tank_rot_1,tank_rot_2,rect1,rect2,new_image1,new_image2
    global done
    while not done:
        rect1.center = (player_x1 // 2, player_y1 // 2)
        rect2.center = (player_x2 // 2, player_y2 // 2)
        keys_pressed = py.key.get_pressed()
        for event in py.event.get():
            if event.type == py.QUIT:
                done = True

        if keys_pressed[py.K_a]:
            player_x1 = (player_x1 + (10 * (math.cos(tank_rot_1))) * 0.3)  # iterations are fixed. So constant length of width which is getting added .
            player_y1 = (player_y1 + (10 * (math.sin(tank_rot_1))) * 0.3)
            draw()

        if not keys_pressed[py.K_a]:
            old_center_1 = rect1.center
            tank_rot_1 = (tank_rot_1 + rot_speed) % 360
            new_image1 = py.transform.rotate(tank1, tank_rot_1)
            rect1 = new_image1.get_rect()
            # set the rotated rectangle to the old center
            rect1.center = old_center_1
            # drawing the rotated rectangle to the screen
            screen.blit(new_image1, rect1)

        # if keys_pressed[py.K_SPACE]:
        #     curr_x1 = player_x1 + 20
        #     curr_y1 = player_y1
        #     while curr_x1<=800 and curr_y1>=0:
        #         curr_y1-=4
        #         if curr_x1<=player_x2+40 and curr_x1>=player_x2:
        #             print('Player1 Wins')
        #             sys.exit(0)
        #         elif curr_y1>curr_y2+4 and curr_y1<curr_y2+4 :   #bullets collision
        #             bullet1(900,900)
        #             bullet2(900, 900)
        #         else:
        #             bullet_1(curr_x1,curr_y1)

        if keys_pressed[py.K_UP]:
            player_x2 = (player_x2 + (10 * (math.cos(tank_rot_2))) * 0.3)  # iterations are fixed. So constant length of width which is getting added .
            player_y2 = (player_y2 + (10 * (math.sin(tank_rot_2))) * 0.3)
            draw()

        if not keys_pressed[py.K_UP]:
            old_center_2 = rect2.center
            tank_rot_2 = (tank_rot_2 + rot_speed) % 360
            new_image2 = py.transform.rotate(tank2, tank_rot_2)
            rect2 = new_image2.get_rect()
            # set the rotated rectangle to the old center
            rect2.center = old_center_2
            # drawing the rotated rectangle to the screen
            screen.blit(new_image2, rect2)

        # if keys_pressed[py.K_l]:
        #     curr_x2=player_x2+20
        #     curr_y2 =player_y2
        #     while curr_x2 <= 800 and curr_y2 <= 800:
        #         curr_y2 += 4
        #         if curr_x2<=player_x1+40 and curr_x2>=player_x1:
        #             print('Player2  Wins')
        #             sys.exit(0)
        #         elif curr_y2>curr_y1+4 and curr_y2<curr_y1+4 :     #bullets collision
        #             bullet1(900,900)
        #             bullet2(900, 900)
        #         else:
        #             bullet_2(curr_x2,curr_y2)
        # #py.draw.rect(screen, (0, 255, 0), py.Rect(0, 680, 800, 120))
        py.display.flip()


if __name__ == '__main__':
    main()

