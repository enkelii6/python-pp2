import pygame, random, time, json, pickle, sys
screen = pygame.display.set_mode((1000, 650))
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Shnake')

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SHADOW = (192, 192, 192)
ORANGE = (255,100,10)
GREY = (127,127,127)
NAVY_BLUE = (0,0,100)
POWDERBLUE = (176, 224, 230, 255)
YELLOW = (255, 255, 0)
PURPLE = (153, 0, 153)

menu_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/mode_setting.png'), (1000, 650))
start_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/start.png'), (200, 50))
start_act_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/start_.png'), (200, 50))
pl1_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/1pl.png'), (200, 50))
pl2_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/2pl.png'), (200, 50))
pl1_act_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/1pl_.png'), (200, 50))
pl2_act_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/2pl_.png'), (200, 50))
exit_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/exit.png'), (200, 50))
exit_act_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/exit_.png'), (200, 50))
newgame_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/newgame.png'), (200, 50))
newgame_act_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/newgame_.png'), (200, 50))
bc_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/bc.png'), (200, 200))
rock_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/Rock Pile.png'), (50, 50))
rock1_png = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/Rock Pile1.png'), (50, 50))
apple_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/apple.png'), (25, 25))
ez_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/ez.png'), (400, 80))
normal_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/norm.png'), (400, 80))
hard_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/hard.png'), (400, 80))
ez_act_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/ez_.png'), (400, 80))
normal_act_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/norm_.png'), (400, 80))
hard_act_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/hard_.png'), (400, 80))
mode_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/mode.png'), (120, 20))
single_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/single.png'), (150, 25))
twoplayer_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/2player.png'), (150, 20))
gamelvl_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/gamelvl.png'), (150, 35))
gamelvl_ez_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/ezzz.png'), (70, 20))
gamelvl_norm_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/normal.png'), (100, 20))
gamelvl_hard_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/hardcore.png'), (100, 20))
score_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/score.png'), (100, 20))
scores_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/scores.png'), (100, 20))
player1_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/player1.png'), (100, 20))
player2_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/player2.png'), (100, 20))
dead_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/dead.png'), (50, 20))
save_img = pygame.transform.scale(pygame.image.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/img/save&quit.png'), (150, 35))


def main_menu():
    global game_started, start_btn, pl1_btn, pl2_btn, exit_btn, menu, newgame_btn
    pygame.mixer_music.load('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/sounds/gta.mp3')
    pygame.mixer_music.play()
    game_started, pl1_mode, pl2_mode, menu = False, False, False, True
    screen.blit(menu_png, (0, 0))
    start_btn = screen.blit(start_png, (400, 250))
    pl1_btn = screen.blit(pl1_png, (250, 325))
    pl2_btn = screen.blit(pl2_png, (550, 325))
    exit_btn = screen.blit(exit_png, (550, 400))
    newgame_btn = screen.blit(newgame_act_png, (250, 400))
    pygame.display.flip()


def mode_choose():
    global ez_btn, normal_btn, hard_btn
    screen.blit(menu_png, (0, 0))
    ez_btn = screen.blit(ez_img, (300, 230))
    normal_btn = screen.blit(normal_img, (300, 330))
    hard_btn = screen.blit(hard_img, (300, 430))


def easy_mode_draw():
    for j in range(0, 650, 200):
        for i in range(0, 1000, 200):
            screen.blit(bc_png, (i, j))
    for n, i in enumerate(range(0, 800, 50), 1):
        screen.blit(rock1_png, (i, 0))
        if n < 15:
            screen.blit(rock_png, (i+50, 600)) 
    for n, j in enumerate(range(0, 650, 50), 1):
        screen.blit(rock1_png, (0, j))
        if n < 13:
            screen.blit(rock_png, (750, j+50))
    

def normal_mode_draw():
    easy_mode_draw()
    for i in range(100, 201, 50):
        screen.blit(rock1_png, (i, 100))
        screen.blit(rock1_png, (i + 450, 100))
        screen.blit(rock_png, (i, 500))
        screen.blit(rock_png, (i + 450, 500))
    for j in range(150, 250, 50):
        screen.blit(rock1_png, (100, j))
        screen.blit(rock1_png, (100, j + 250))
        screen.blit(rock_png, (650, j))
        screen.blit(rock_png, (650, j + 250))



def hard_mode_draw():
    normal_mode_draw()
    for i in range(200, 600, 50):
        screen.blit(rock1_png, (i, 200))
        screen.blit(rock_png, (i, 400))
    screen.blit(rock_png, (200, 250))
    screen.blit(rock1_png, (200, 350))
    screen.blit(rock_png, (550, 250))
    screen.blit(rock1_png, (550, 350))



def normal_mode_collision(x, y):
    if (100 <= x <= 250 or 550 <= x <= 700) and (100 <= y <= 150 or 500 <= y <= 550):
        return True
    if (100 <= x <= 150 or 650 <= x <= 700) and (150 <= y <= 250 or 400 <= y <= 500):
        return True


normal_mode_area_x = [i for i in range(50, 76, 1)] + [i for i in range(251, 526, 1)] + [i for i in range(701, 730, 1)]
normal_mode_area_y = [i for i in range(50, 75, 1)] + [i for i in range(155, 375, 1)] + [i for i in range(555, 576, 1)]



def hard_mode_collision(x, y):
    if 200 <= x <= 600 and (200 <= y <= 250 or 400 <= y <= 450):
        return True
    if (200 <= x <= 250 or 550 <= x <= 600) and (250 <= y <= 300 or 350 <= y <= 400):
        return True



def game_status(dead1, dead2):
    global player, mode, score1, score2, save_quit, data
    font = pygame.font.SysFont('verdana', 23)
    font1 = pygame.font.SysFont('verdana', 21)
    screen.blit(mode_img, (810, 350))

    if data['player'] == '1':
        screen.blit(single_img, (830, 380))
        screen.blit(score_img, (810, 30))
        score1_txt = font.render(str(data['score1']), True, (204, 204, 255))
        screen.blit(score1_txt, (920, 26))
    elif data['player'] == '2':
        screen.blit(twoplayer_img, (830, 380))
        screen.blit(scores_img, (810, 30))
        screen.blit(player1_img, (830, 80))
        screen.blit(player2_img, (830, 130))
        if not dead1:
            score1_txt = font1.render(str(data['score1']), True, (204, 204, 255))
            screen.blit(score1_txt, (940, 76))
        else:
            screen.blit(dead_img, (940, 78))
        
        if not dead2:
            score2_txt = font1.render(str(data['score2']), True, (204, 204, 255))
            screen.blit(score2_txt, (940, 125))
        else:
            screen.blit(dead_img, (938, 127))

    screen.blit(gamelvl_img, (810, 230))

    save_quit = screen.blit(save_img, (820, 580))

    if data['mode'] == 'easy':
        screen.blit(gamelvl_ez_img, (850, 280))
    elif data['mode'] == 'normal':
        screen.blit(gamelvl_norm_img, (840, 280))
    elif data['mode'] == 'hard':
        screen.blit(gamelvl_hard_img, (837, 280)) 


hard_x1 = [i for i in range(53, 75, 1)] + [i for i in range(603, 625, 1)] + [i for i in range(703, 725, 1)]
hard_x2 = [i for i in range(53, 175, 1)] + [i for i in range(253, 525, 1)] + [i for i in range(603, 725, 1)]
hard_x3 = [i for i in range(53, 75, 1)] + [i for i in range(153, 675, 1)] + [i for i in range(703, 725, 1)] 
hard_x4 = [i for i in range(53, 75, 1)] + [i for i in range(253, 525, 1)] + [i for i in range(703, 725)]



class Food:
    def __init__(self):
        self.x = 350
        self.y = 300
        self.rect = screen.blit(apple_img, (self.x, self.y))

    def gen(self):
        if data['mode'] == 'easy':
            self.x = random.randint(50, 730)
            self.y = random.randint(50, 576)
        elif data['mode'] == 'normal':
            self.x = random.choice(normal_mode_area_x)
            self.y = random.choice(normal_mode_area_y)
        elif data['mode'] == 'hard':
            while True:
                self.y = random.randint(50, 576)
                if 50 <= self.y <= 75 or 550 <= self.y <= 575:
                    self.x = random.randint(50, 730)
                    break
                if 100 <= self.y <= 125 or 500 <= self.y <= 525:
                    self.x = random.choice(hard_x4)
                    break
                if 150 <= self.y <= 175 or 450 <= self.y <= 475:
                    self.x = random.choice(hard_x3)
                    break
                if 200 <= self.y <= 225 or 400 <= self.y <= 425:
                    self.x = random.choice(hard_x1)
                    break
                if 250 <= self.y <= 275 or 350 <= self.y <= 375:
                    self.x = random.choice(hard_x2)
                    break


    def draw(self):
        self.rect = screen.blit(apple_img, (self.x, self.y))



class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]
        self.radius = 10
        self.dx = 5
        self.dy = 0
        self.is_add = False
        self.speed = 30
        self.dead = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (200,190,140), element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 10 == 0:
            self.speed += 3


    def move(self):

        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0,-1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

        if [self.elements[0][0],self.elements[0][1]] in self.elements[1:]:
            self.dead = True

        if self.elements[0][0] > 750 - self.radius:
            self.dead = True
        elif self.elements[0][0] < 50 + self.radius:
            self.dead = True

        if self.elements[0][1] > 600 - self.radius:
            self.dead = True
        elif self.elements[0][1] < 50 + self.radius:
            self.dead = True


    def eat(self, rect):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if rect.collidepoint(x, y):
            return True

    def two_snakes_collid(self, x, y):
        if [x, y] in self.elements[1:]:
            return True


def uh_sound():
    pygame.mixer.Sound('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/sounds/dead.mp3').play()


def click_sound():
    pygame.mixer.Sound('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/sounds/click.mp3').play()

def eat_sound():
    pygame.mixer.Sound('/Users/Gleb/Desktop/pp2/python-pp2/labs/lab8and9/snake/sounds/eat.mp3').play()


global snake1, snake2, food, snakes
snake1 = Snake(100, 70)
snake2 = Snake(150, 100)
food = Food()
snakes = [snake1, snake2]


global data
data = {
    'score1' : 0,
    'score2' : 0,
    'mode' : 'none',
    'player' : 'none'
}


def load_settings():
    global data
    with open('local_data.txt', 'r') as f:
        data = json.load(f)


def save_object_snake(objlist, n):
    if n == '1':
        with open('snake1.pkl', 'wb') as output:
            pickle.dump(objlist[0], output, pickle.HIGHEST_PROTOCOL)
    else:
        with open('snake2.pkl', 'wb') as output:
            pickle.dump(objlist[1], output, pickle.HIGHEST_PROTOCOL)

        with open('snake1.pkl', 'wb') as output:
            pickle.dump(objlist[0], output, pickle.HIGHEST_PROTOCOL)


def load_object_snake(objlist, n):
    if n == '1':
        with open('snake1.pkl', 'rb') as input:
            objlist[0] = pickle.load(input)
    else:
        with open('snake2.pkl', 'rb') as input:
            objlist[1] = pickle.load(input)

        with open('snake1.pkl', 'rb') as input:
            objlist[0] = pickle.load(input)

main_menu()

global menu, d, running, clicked
clicked = False
d, menu = 5, True
running = True

while running:
    global start_btn, game_started, pl1_btn, pl2_btn, exit_btn, ez_btn, normal_btn, hard_btn, newgame_btn, save_quit
    clock.tick(snake1.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            x, y = event.pos


            if data['mode'] == 'choosing' and ez_btn.collidepoint(x, y):
                click_sound()
                screen.blit(ez_act_img, (300, 230))
                pygame.display.flip()
                time.sleep(1)
                data['mode'] = 'easy'
                menu = False
                snake1 = Snake(100, 70)
                snake2 = Snake(200, 70)
                snakes = [snake1, snake2]
                food = Food()
                game_started = True

            if data['mode'] == 'choosing' and normal_btn.collidepoint(x, y):
                click_sound()
                screen.blit(normal_act_img, (300, 330))
                pygame.display.flip()
                time.sleep(1)
                data['mode'] = 'normal'
                menu = False
                snake1 = Snake(100, 70)
                snake2 = Snake(200, 70)
                snakes = [snake1, snake2]
                food = Food()
                game_started = True

            if data['mode'] == 'choosing' and hard_btn.collidepoint(x, y):
                click_sound()
                screen.blit(hard_act_img, (300, 430))
                pygame.display.flip()
                time.sleep(1)
                data['mode'] = 'hard'
                menu = False
                snake1 = Snake(100, 70)
                snake2 = Snake(200, 70)
                snakes = [snake1, snake2]
                food = Food()
                game_started = True


            if menu:
                if newgame_btn.collidepoint(x, y) and not clicked:
                    click_sound()
                    screen.blit(newgame_png, (250, 400))
                    screen.blit(pl2_png, (550, 325))
                    screen.blit(pl1_png, (250, 325))
                    clicked = True
                elif newgame_btn.collidepoint(x, y) and clicked:
                    click_sound()
                    screen.blit(newgame_act_png, (250, 400))
                    clicked = False
                    
                if exit_btn.collidepoint(x, y):
                    click_sound()
                    screen.blit(exit_act_png, (550, 400))
                    running = False
                    time.sleep(0.8)

                if start_btn.collidepoint(x, y):
                    if clicked:
                        load_settings()
                        click_sound()
                        screen.blit(start_act_png, (400, 250))
                        pygame.display.flip()
                        load_object_snake(snakes, data['player'])
                        food = Food()
                        food.x = data['food.x']
                        food.y = data['food.y']
                        menu = False
                        game_started = True
                        time.sleep(1)
                    
                    elif data['player'] != 'none':
                        click_sound()
                        screen.blit(start_act_png, (400, 250))
                        pygame.display.flip()
                        time.sleep(1)
                        data['mode'] = 'choosing'
                        mode_choose()


                if pl1_btn.collidepoint(x, y) and (data['player'] == 'none' or data['player'] != '1') and data['mode'] == 'none':
                    click_sound()
                    screen.blit(pl2_png, (550, 325))
                    screen.blit(pl1_act_png, (250, 325))
                    data['player'] = '1'

                if pl2_btn.collidepoint(x, y) and (data['player'] == 'none' or data['player'] != '2') and data['mode'] == 'none':
                    click_sound()
                    screen.blit(pl1_png, (250, 325))
                    screen.blit(pl2_act_png, (550, 325))
                    data['player'] = '2'


        if event.type == pygame.KEYDOWN and game_started:
            if game_started and event.key == pygame.K_ESCAPE:
                game_started = False

                data['food.x'] = food.x
                data['food.y'] = food.y
                with open('local_data.txt', 'w') as f:
                    json.dump(data, f)

                save_object_snake(snakes, data['player'])
                menu = True
                main_menu()

            if event.key == pygame.K_RIGHT and snake1.dx != -d:
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_LEFT and snake1.dx != d:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_UP and snake1.dy != d:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_DOWN and snake1.dy != -d:
                snake1.dx = 0
                snake1.dy = d

            if event.key == ord('d') and snake2.dx != -d:
                snake2.dx = d
                snake2.dy = 0
            if event.key == ord('a') and snake2.dx != d:
                snake2.dx = -d
                snake2.dy = 0
            if event.key == ord('w') and snake2.dy != d:
                snake2.dx = 0
                snake2.dy = -d
            if event.key == ord('s') and snake2.dy != -d:
                snake2.dx = 0
                snake2.dy = d


    if game_started and not menu:

        if data['player'] == '2':
            if snake1.eat(food.rect):
                data['score1'] += 1
                eat_sound()
                snake1.is_add = True
                food.gen()

            if snake2.eat(food.rect):
                data['score2'] += 1
                eat_sound()
                snake2.is_add = True
                food.gen()

            if data['mode'] == 'easy':
                easy_mode_draw()
            elif data['mode'] == 'normal':
                normal_mode_draw()
            elif data['mode'] == 'hard':
                hard_mode_draw()

            game_status(snake1.dead, snake2.dead)

            if data['mode'] != 'easy':
                if normal_mode_collision(snake1.elements[0][0], snake1.elements[0][1]):
                    snake1.dead = True
                    uh_sound()
                if normal_mode_collision(snake2.elements[0][0], snake2.elements[0][1]):
                    uh_sound()
                    snake2.dead = True
                if data['mode'] == 'hard':
                    if hard_mode_collision(snake1.elements[0][0], snake1.elements[0][1]):
                        uh_sound()
                        snake1.dead = True
                    if hard_mode_collision(snake2.elements[0][0], snake2.elements[0][1]):
                        uh_sound()
                        snake2.dead = True
            
            if snake1.two_snakes_collid(snake2.elements[0][0], snake2.elements[0][1]):
                    uh_sound()
                    snake2.dead = True

            if snake2.two_snakes_collid(snake1.elements[0][0], snake1.elements[0][1]):
                    uh_sound()
                    snake1.dead = True


            if not snake1.dead:
                snake1.move()
                snake1.draw()
            if not snake2.dead:
                snake2.move()
                snake2.draw()

            food.draw()

            if snake1.dead and snake2.dead:
                time.sleep(1)
                game_started = False
                menu = True
                data['mode'] = 'none'
                data['player'] = 'none'
                snake1.dead = False
                snake2.dead = False
                main_menu()


        if data['player'] == '1':
            if snake1.eat(food.rect):
                data['score1'] += 1
                eat_sound()
                snake1.is_add = True
                food.gen()
            
            snake1.move()

            if data['mode'] == 'easy':
                easy_mode_draw()
            elif data['mode'] == 'normal':
                normal_mode_draw()
            elif data['mode'] == 'hard':
                hard_mode_draw()

            game_status(snake1.dead, snake2.dead)
            snake1.draw()
            food.draw()

            if data['mode'] != 'easy':
                if normal_mode_collision(snake1.elements[0][0], snake1.elements[0][1]):
                    uh_sound()
                    snake1.dead = True
                if data['mode'] == 'hard':
                    if hard_mode_collision(snake1.elements[0][0], snake1.elements[0][1]):
                        uh_sound()
                        snake1.dead = True

            if snake1.dead:
                uh_sound()
                time.sleep(1)
                game_started = False
                menu = True
                data['mode'] = 'none'
                data['player'] = 'none'
                snake1.dead = False
                if clicked:
                    clicked = False
                main_menu()
    pygame.display.flip()

pygame.quit()