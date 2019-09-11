import pygame as py
import os,sys,random
import numpy as np
import math

screen = py.display.set_mode((800, 800))
py.init()
done = False
cord = [(random.randint(40,800),random.randint(40,800)) for i in range(30)]   #array of co ordinates
background = py.image.load('background.jpg')
obstacle = py.image.load('rock.png')
tankxx = py.image.load('realtank.png')


#creating the tank Dictionary to store the two tanks.
Tank = {
    'tank1':{
        'image':py.image.load('realtank.png'),
        'bullet':{
            'image':py.image.load('missile.png'),
            'x':25,
            'y':25 
        }, 
        'rect':tankxx.get_rect(),
        'new_image':py.image.load('realtank.png'),
        'old_center':(25,25),
        'angle':0
     },
    'tank2':{
        'image':  py.image.load('realtank.png'),
        'bullet':{
            'image':py.image.load('missile.png'),
            'x':750,
            'y':750 
        }, 
        'rect':tankxx.get_rect(),
        'new_image':py.image.load('realtank.png'),
        'old_center':(750,750),
        'angle':0
    }
}

#setting the initial position of the tanks.
Tank['tank1']['rect'].center = (25,25)
Tank['tank2']['rect'].center = (750,750)


print('Type is:',Tank['tank1']['rect'])
#getting type as pygame.rect.....


def draw_obstacles(screen):
    for i,j in cord:
        screen.blit(obstacle, (i, j))

def tank_win_check(bulletx,bullety,index):
    global Tank
    lose = False
    if index=='tank1':
        index='tank2'
    else:
        index='tank1'
    
    (tank_x , tank_y )= Tank[index]['rect'].center
    equation = lambda x, y: (x - tank_x) ** 2 + (y - tank_y) ** 2 - 400
    if equation(bulletx,bullety)<=0:
        lose = True
        return lose

    return False

def bullet_check(bulletx,bullety):
    movable = True

    for i,j in cord:
        obs_x=i+14
        obs_y=j+14
        equation = lambda x,y: (x-obs_x)**2 + (y-obs_y)**2 - 256
        if equation(bulletx,bullety) <= 0:
            movable = False
            break
        else:
            movable = True

    return movable

def tank_obstacle_check(tankx,tanky):
    movable = True
    for i, j in cord:
        obs_x = i + 25
        obs_y = j + 25  #added for extra obstruction
        equation = lambda x, y: (x - obs_x) ** 2 + (y - obs_y) ** 2 - 625
        if equation(tankx, tanky) <= 0:
            movable = False
            break
        else:
            movable = True

    return movable

def draw():
    global Tank
    screen = py.display.set_mode((800,800))
    #screen.blit(background,[0,0])               #setting the background image
    draw_obstacles(screen)
    print('New Rect', Tank['tank1']['rect'])
    screen.blit(Tank['tank1']['new_image'],Tank['tank1']['rect'])  # setting the tank1 pos
    screen.blit(Tank['tank2']['new_image'],Tank['tank2']['rect'])
    py.display.flip()  # usded to view the updates on screen as soon as we see them.

def rotate(clock,tank):
    global Tank
    screen = py.display.set_mode((800, 800))
    #screen.blit(background,[0,0]) 
    draw_obstacles(screen)
    tank['rect'] = tankxx.get_rect()
    tank['old_center'] = tank['rect'].center
    tank['angle'] = (tank['angle'] + (clock)*3) % 360
    tank['new_image'] = py.transform.rotate(tank['image'],tank['angle'])
    new_img_temp = tank['new_image']
    tank['rect'] = new_img_temp.get_rect()
    tank['rect'].center = tank['old_center']
    #isko ese hi rakhe na?
    #haa chalega
    screen.blit(Tank['tank1']['new_image'],Tank['tank1']['rect'])
    screen.blit(Tank['tank2']['new_image'],Tank['tank2']['rect'])
    py.display.flip()


def bullet(bullet_x,bullet_y,index):
    global Tank
    screen = py.display.set_mode((800,800))
    #screen.blit(background,[0,0]) 
    draw_obstacles(screen)
    screen.blit(Tank['tank1']['new_image'],Tank['tank1']['rect'])  # setting the tank1 pos
    screen.blit(Tank['tank2']['new_image'],Tank['tank2']['rect'])
    screen.blit(Tank[index]['bullet']['image'],(Tank[index]['bullet']['x'],Tank[index]['bullet']['y']))
    py.display.flip()


def main():
    global Tank
    global player_x1, player_y1,player_x2, playecer_y2
    global done

    while not done:
        keys_pressed = py.key.get_pressed()

        for event in py.event.get():
            if event.type == py.QUIT:
                done = True


        #moving the first tank anti-clockwise
        if keys_pressed[py.K_a]:
            rotate(1,Tank['tank1'])
            draw()
        # moving the first tank clockwise
        if keys_pressed[py.K_d]:
            rotate(-1,Tank['tank1'])
            draw()

        #translation motion for the first tank.
        if keys_pressed[py.K_w]:
            Tank['tank1']['rect'] = Tank['tank1']['new_image'].get_rect()
            (player_x1,player_y1) = Tank['tank1']['rect'].center
            #print('Inside and b4',Tank['tank1']['rect'].center)
            const_length = 4
            rad_to_deg = math.pi/180
            temp_x_1 = player_x1 + const_length * math.cos(Tank['tank1']['angle'] * rad_to_deg)
            temp_y_1 = player_y1 - const_length * math.sin(Tank['tank1']['angle'] * rad_to_deg)
            tank_movable_1 = tank_obstacle_check(temp_x_1,temp_y_1)
            print(tank_movable_1)
            if tank_movable_1:
                player_x1 = temp_x_1
                player_y1 = temp_y_1
                Tank['tank1']['rect'] = Tank['tank1']['new_image'].get_rect()
                Tank['tank1']['rect'].center = (player_x1,player_y1)
                #print('Inside and after',Tank['tank1']['rect'].center)
                print('Old Rect ', Tank['tank1']['rect'])
            draw()

        #check if the value of center is changing or not
        #ok
        #bullet from tank1
        if keys_pressed[py.K_e]:
            Tank['tank1']['rect'] = Tank['tank1']['new_image'].get_rect()
            bullet_x1, bullet_y1 =Tank['tank1']['rect'].center
            while 0 < bullet_x1 < 800 and 0 < bullet_y1 < 800:
                const_length = 4
                rad_to_deg = math.pi / 180
                bullet_x1 += const_length * math.cos(Tank['tank1']['angle']* rad_to_deg)
                bullet_y1 -= const_length * math.sin(Tank['tank1']['angle']* rad_to_deg)
                movable_1 = bullet_check(bullet_x1,bullet_y1)
                win1 = tank_win_check(bullet_x1,bullet_y1,'tank1')
                if win1:
                    print('Player 1 wins')
                    sys.exit(0)
                if movable_1:
                    bullet(bullet_x1, bullet_y1,'tank1')
                else:
                    break

        #moving the second tank anti-clockwise
        if keys_pressed[py.K_LEFT]:
            rotate(1,Tank['tank2'])
            draw()
        # moving the second tank clockwise
        if keys_pressed[py.K_RIGHT]:
            rotate(-1,Tank['tank1'])
            draw()


        #translation motion for the second tank.
        if keys_pressed[py.K_UP]:
            Tank['tank2']['rect'] =  Tank['tank2']['new_image'].get_rect()
            player_x2,player_y2 = Tank['tank2']['rect'].center
            const_length = 4
            rad_to_deg = math.pi/180
            temp_x_2 = player_x2 + const_length * math.cos(Tank['tank2']['angle']*rad_to_deg)
            temp_y_2 = player_y2 - const_length * math.sin(Tank['tank2']['angle'] * rad_to_deg)
            tank_movable_2 = tank_obstacle_check(temp_x_2,temp_y_2)
            if tank_movable_2:
                player_x2 += temp_x_2
                player_y2 -= temp_y_2
                Tank['tank2']['rect'].center = (player_x2,player_y2)
            draw()

        #bullet from tank2
        if keys_pressed[py.K_l]:
            Tank['tank2']['rect'] =  Tank['tank2']['new_image'].get_rect()
            bullet_x2, bullet_y2 =Tank['tank2']['rect'].center
            while 0 < bullet_x1 < 800 and 0 < bullet_y1 < 800:
                rb2 = 4
                rad_to_deg = math.pi / 180
                bullet_x2 += rb2 * math.cos(Tank['tank2']['angle']* rad_to_deg)
                bullet_y2 -= rb2 * math.sin(Tank['tank2']['angle']* rad_to_deg)
                movable_2 = bullet_check(bullet_x2,bullet_y2)
                win2 = tank_win_check(bullet_x2,bullet_y2,'tank2')
                if win2:
                    print('Player 2 wins')
                    sys.exit(0)
                if movable_2:
                    bullet(bullet_x2, bullet_y2,'tank2')
                else:
                    break

        py.display.flip()


if __name__ == '__main__':
    main()

