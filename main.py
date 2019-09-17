import pygame as py
import sys, random, math

screen = py.display.set_mode((800,800))
py.init()
tank_image1 = py.image.load('tank_green.png')
tank_image2 = py.image.load('tank_red.png')
obstacle_image = py.image.load('rock.png')
bullet_image = py.image.load('missile.png')

tank_dimensions = tank_image1.get_size()
obstacle_dimensions = obstacle_image.get_size()
bullet_dimensions = bullet_image.get_size()

game_clock = py.time.Clock()

tank_rect = tank_image1.get_rect()
color = (0,0,0)

Tank = {
    'tank1' : {
        'image' : tank_image1,
        'new_image' : tank_image1,
        'rect' : tank_image1.get_rect().copy(),
        'center' : (25,25),
        'angle' : 0,
        'bullet' : {
            'image' : bullet_image,
            'rect' : bullet_image.get_rect()
        }
    },

    'tank2' : {
        'image' : tank_image2,
        'new_image' : tank_image2,
        'rect' : tank_image2.get_rect().copy(),
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
obstacles = [(random.randint(40,700),random.randint(40,700)) for i in range(30)]

#checks if the point x,y lies in the circle (x-x1)^2 + (y-y1)^2 = r^2
def collision(x,y,x1,y1,r,is_tank):
    if is_tank:
        r += tank_dimensions[0]/2
    term = (x-x1)**2 + (y-y1)**2
    return term <= r**2

def obstacle_collision(x,y,is_tank):
    radius_obstacle = obstacle_dimensions[0]/2
    for i,j in obstacles:
        i,j = i+radius_obstacle, j+radius_obstacle
        if collision(x,y,i,j,radius_obstacle,is_tank):
            return True
    return False

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
    tank['new_image'] = py.transform.rotate(tank['image'], tank['angle'])
    tank['rect'] = tank['new_image'].get_rect()
    tank['rect'].center = tank['center']

def translate(tank, direction):
    r = 2
    x,y = tank['center']
    x += r*math.cos(math.radians(tank['angle']))*direction
    y -= r*math.sin(math.radians(tank['angle']))*direction
    boundary_condition = (0<x<800) and (0<y<800)
    if obstacle_collision(x,y,True) or not boundary_condition:
        return
    if Tank['tank1'] == tank:
        center_tank = Tank['tank2']['center']
    else:
        center_tank = Tank['tank1']['center']

    width, height = tank_dimensions[0], tank_dimensions[1]
    condition1 = (center_tank[0]-width/2 < x < center_tank[0]+width/2)
    condition2 = (center_tank[1]-height/2 < y < center_tank[1]+height/2)
    if condition1 and condition2:
        return
    tank['center'] = (x,y)
    tank['rect'].center = (x,y)

def bullet_translate(bullet, tank):
    bullet['rect'].center = tank['center']
    x,y = bullet['rect'].center
    r = 10
    while 0 < x < 800 and 0 < y < 800:
        x += r*math.cos(math.radians(tank['angle']))
        y -= r*math.sin(math.radians(tank['angle']))
        if obstacle_collision(x,y,False):
            return
        if Tank['tank1'] == tank:
            center_tank = Tank['tank2']['center']
        else:
            center_tank = Tank['tank1']['center']

        width, height = tank_dimensions[0], tank_dimensions[1]
        condition1 = (center_tank[0]-width/2 < x < center_tank[0]+width/2)
        condition2 = (center_tank[1]-height/2 < y < center_tank[1]+height/2)
        if condition1 and condition2:
            if Tank['tank1'] == tank:
                print("Player 1 Wins")
                sys.exit(0)
            else:
                print("Player 2 Wins")
                sys.exit(0)
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
        translate(Tank['tank1'],1)
    if keys_pressed[py.K_UP]:
        translate(Tank['tank2'],1)
    if keys_pressed[py.K_s]:
        translate(Tank['tank1'],-1)
    if keys_pressed[py.K_DOWN]:
        translate(Tank['tank2'],-1)
    
    #bullet-fire
    if shots_fired1:
        bullet_translate(Tank['tank1']['bullet'], Tank['tank1'])
    if shots_fired2:
        bullet_translate(Tank['tank2']['bullet'], Tank['tank2'])
    
    game_clock.tick(30)

