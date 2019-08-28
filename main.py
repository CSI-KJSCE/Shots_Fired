import pygame as py
import os
import sys

#bullets collision
#obj collision


player_x1 = 50
player_y1 = 50

player_x2 = 750
player_y2 = 750

curr_x1 = player_x1 + 20
curr_y1 = player_y1

curr_y2 =player_y2
curr_x2 = player_x2 + 20
py.init()
done = False
tank1 = py.image.load('tank1.jpg')    #hero size is 40x40
tank2 = py.image.load('tank1.jpg')    #image size is 40x40
bullet1 = py.image.load('bullet1.png')
bullet2 = py.image.load('bullet1.png')


def draw():
    screen = py.display.set_mode((800,800))
    screen.blit(tank1,(player_x1,player_y1))     #setting the tank1 pos
    screen.blit(tank2,(player_x2, player_y2))    #setting the tank2 pos
    py.display.flip()  # used to view the updates on screen as soon as we see them.

def bullet_1(bullet_x,bullet_y):
    screen = py.display.set_mode((800,800))
    screen.blit(tank1, (player_x1, player_y1))  # setting the tank1 pos
    screen.blit(tank2, (player_x2, player_y2))
    screen.blit(bullet1,(bullet_x,bullet_y))
    py.display.flip()

def bullet_2(bullet_x,bullet_y):
    screen = py.display.set_mode((800,800))
    screen.blit(tank1, (player_x1, player_y1))  # setting the tank1 pos
    screen.blit(tank2, (player_x2, player_y2))
    screen.blit(bullet2,(bullet_x,bullet_y))
    py.display.flip()

def main():
    draw()
    global player_x1, player_y1,player_x2, player_y2,curr_y1,curr_y2,curr_x1,curr_x2
    global done

    while not done:
        keys_pressed = py.key.get_pressed()
        for event in py.event.get():
            if event.type == py.QUIT:
                done = True

        if keys_pressed[py.K_d]:
            player_x1 += 3
            draw()
        if keys_pressed[py.K_w]:
            player_y1 -= 3
            draw()
        if keys_pressed[py.K_a]:
            player_x1 -= 3
            draw()
        if keys_pressed[py.K_s]:
            player_y1 += 3
            draw()


        if(keys_pressed[py.K_SPACE]):
            curr_x1 = player_x1 + 20
            curr_y1 = player_y1
            while curr_x1<=800 and curr_y1>=0:
                curr_y1-=4
                if curr_x1<=player_x2+40 and curr_x1>=player_x2:
                    print('Player1 Wins')
                    sys.exit(0)
                elif curr_y1>curr_y2+4 and curr_y1<curr_y2+4 :   #bullets collision
                    bullet1(900,900)
                    bullet2(900, 900)
                else:
                    bullet_1(curr_x1,curr_y1)

        if keys_pressed[py.K_RIGHT]:
            player_x2 += 3
            draw()
        if keys_pressed[py.K_UP]:
            player_y2 -= 3
            draw()
        if keys_pressed[py.K_LEFT]:
            player_x2 -= 3
            draw()
        if keys_pressed[py.K_DOWN]:
            player_y2 += 3
            draw()

        if keys_pressed[py.K_l]:
            curr_x2=player_x2+20
            curr_y2 =player_y2
            while curr_x2 <= 800 and curr_y2 <= 800:
                curr_y2 += 4
                if curr_x2<=player_x1+40 and curr_x2>=player_x1:
                    print('Player2  Wins')
                    sys.exit(0)
                elif curr_y2>curr_y1+4 and curr_y2<curr_y1+4 :     #bullets collision
                    bullet1(900,900)
                    bullet2(900, 900)
                else:
                    bullet_2(curr_x2,curr_y2)
        #py.draw.rect(screen, (0, 255, 0), py.Rect(0, 680, 800, 120))


if __name__ == '__main__':
    main()

