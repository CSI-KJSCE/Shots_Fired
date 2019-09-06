import pygame as py
import sys,random
import math

screen = py.display.set_mode((800, 800))
tank_rot_1= 0
tank_rot_2= 0


py.init()
done = False


cord = [(random.randint(40,800),random.randint(40,800)) for i in range(30)]   #array of co ordinates

tank1 = py.image.load('realtank.png')
tank2 = py.image.load('realtank.png')    #image size is 40x40
bullet1 = py.image.load('missile.png')
bullet2 = py.image.load('missile.png')
background = py.image.load('background.jpg')
obstacle = py.image.load('rock.png')

rect1 = tank1.get_rect()
rect2 = tank2.get_rect()

rect1.center = (25,25)
rect2.center =(500,500)

new_image_1 = tank1
new_image_2 = tank2

def draw_obstacles(screen):
    for i,j in cord:
        screen.blit(obstacle, (i, j))

def tank_1_win_check(bulletx,bullety):
    lose = False
    (tank_2_x , tank_2_y )= rect2.center
    equation = lambda x, y: (x - tank_2_x) ** 2 + (y - tank_2_y) ** 2 - 400
    if equation(bulletx,bullety)<=0:
        lose = True
        return lose

    return False

def tank_2_win_check(bulletx,bullety):
    lose = False
    (tank_1_x , tank_1_y )= rect1.center
    equation = lambda x, y: (x - tank_1_x) ** 2 + (y - tank_1_y) ** 2 - 400
    if equation(bulletx,bullety)<=0:
        lose = True
        return lose

    return False

def bullet_check_1(bulletx,bullety):
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


def bullet_check_2(bulletx,bullety):
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

def tank_obstacle_check_1(tankx,tanky):
    movable = True
    for i, j in cord:
        r=25
        obs_x = i + r
        obs_y = j + r  #added for extra obstruction
        equation = lambda x, y: (x - obs_x) ** 2 + (y - obs_y) ** 2 - r**2
        if equation(tankx, tanky) <= 0:
            movable = False
            break
        else:
            movable = True

    return movable


def tank_obstacle_check_2(tankx,tanky):
    movable = True
    for i, j in cord:
        r=25
        obs_x = i + r
        obs_y = j + r  #added for extra obstruction
        equation = lambda x, y: (x - obs_x) ** 2 + (y - obs_y) ** 2 - r**2
        if equation(tankx, tanky) <= 0:
            movable = False
            break
        else:
            movable = True

    return movable


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
    tank_rot_1 = (tank_rot_1 + (clock)*3) % 360
    new_image_1 = py.transform.rotate(tank1,tank_rot_1)
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
    tank_rot_2 = (tank_rot_2 + (clock)*3) % 360
    new_image_2 = py.transform.rotate(tank2,tank_rot_2)
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
    global player_x1, player_y1,player_x2, player_y2,curr_y1,curr_y2,curr_x1,curr_x2,tank1,tank2,tank_rot_1,tank_rot_2
    global rect1,rect2,new_image1,new_image2
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
            r1 = 2
            rad_to_deg = math.pi/180
            temp_x_1 = player_x1 + r1*math.cos(tank_rot_1*rad_to_deg)
            temp_y_1 = player_y1 - r1*math.sin(tank_rot_1 * rad_to_deg)
            tank_movable_1 = tank_obstacle_check_1(temp_x_1,temp_y_1)
            if tank_movable_1:
                player_x1 += r1 * math.cos(tank_rot_1*rad_to_deg)
                player_y1 -= r1 * math.sin(tank_rot_1*rad_to_deg)
                rect1.center = (player_x1,player_y1)
            draw()

        #bullet from tank1
        if keys_pressed[py.K_e]:
            bullet_x1, bullet_y1 = rect1.center
            while 0 < bullet_x1 < 800 and 0 < bullet_y1 < 800:
                rb1 = 2
                rad_to_deg = math.pi / 180
                bullet_x1 += rb1 * math.cos(tank_rot_1 * rad_to_deg)
                bullet_y1 -= rb1 * math.sin(tank_rot_1 * rad_to_deg)
                movable_1 = bullet_check_1(bullet_x1,bullet_y1)
                win1 = tank_1_win_check(bullet_x1,bullet_y1)
                if win1:
                    print('Player 1 wins')
                    sys.exit(0)
                if movable_1:
                    bullet_1(bullet_x1, bullet_y1)
                else:
                    break

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
            r2 = 2
            rad_to_deg = math.pi / 180
            temp_x_2 = player_x2 + r2 * math.cos(tank_rot_2 * rad_to_deg)
            temp_y_2 = player_y2 - r2 * math.sin(tank_rot_2 * rad_to_deg)
            tank_movable_2 = tank_obstacle_check_1(temp_x_2, temp_y_2)
            if tank_movable_2:
                player_x2 += r2 * math.cos(tank_rot_2 * rad_to_deg)
                player_y2 -= r2 * math.sin(tank_rot_2 * rad_to_deg)
                rect2.center = (player_x2, player_y2)
            draw()

        #bullet from tank2:
        if keys_pressed[py.K_l]:
            bullet_x2, bullet_y2 = rect2.center
            while 0 < bullet_x2 < 800 and 0 < bullet_y2 < 800:
                rb2 = 2
                rad_to_deg = math.pi / 180
                bullet_x2 += rb2 * math.cos(tank_rot_2 * rad_to_deg)
                bullet_y2 -= rb2 * math.sin(tank_rot_2 * rad_to_deg)
                bullet_2(bullet_x2, bullet_y2)
                movable_2 = bullet_check_2(bullet_x2, bullet_y2)
                win2 = tank_2_win_check(bullet_x2, bullet_y2)
                if win2:
                    print('Player 2 wins')
                    sys.exit(0)
                if movable_2:
                    bullet_2(bullet_x2, bullet_y2)
                else:
                    break
        py.display.flip()


if __name__ == '__main__':
    main()

