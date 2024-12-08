import pygame
import random
import os

pygame.init()

pygame.mixer.init()

#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

#creating window
screen_width = 720
screen_height = 550
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#background image 
bgmi= pygame.image.load("SUMIT.png")
bgmi= pygame.transform.scale(bgmi, (screen_width, screen_height)).convert_alpha()
bgg = pygame.image.load("bg.jpg")
bgg = pygame.transform.scale(bgg, (screen_width, screen_height)).convert_alpha()
out = pygame.image.load("outro.png")
out = pygame.transform.scale(out, (screen_width, screen_height)).convert_alpha()

#game title
pygame.display.set_caption("SnakesWithSumit")
pygame.display.update()


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
fps = 40

#creating a Home Screen/Welcome Screen
def Welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(black)
        gameWindow.blit(bgmi, (0,0))
        text_screen("WELCOME TO SNAKES ", red, 190, 260)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('back.mp3')
                        pygame.mixer.music.play()
                        game_loop()
        pygame.display.update()
        clock.tick(fps)
#Game loop
def game_loop():

    #Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, int(screen_width/2))
    food_y = random.randint(20, int(screen_height/2))
    snake_size = 18
    food_size = 19
    init_velocity = 5
    score = 0

    snk_list =[]
    snake_length = 1

    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
                f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            gameWindow.fill(black)
            gameWindow.blit(out, (0,0))
            text_screen("Score: "+str(score), red, 275, 350)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RETURN:
                        Welcome()
            pygame.display.update()
            clock.tick(fps)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                        
                    if event.key == pygame.K_q:
                        score+=10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score += 10
                food_x = random.randint(20, int(screen_width/2))
                food_y = random.randint(20, int(screen_height/2))
                snake_length += 5

                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgg, (0,0))
            text_screen("Score: "+ str(score) +"  HighScore: "+ str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])

            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snake_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
Welcome()