from snake import Snake
import pygame, random, time


# Função para mudar direção da cobra
def set_direction(previous_direction):
    keys = pygame.key.get_pressed()

    directions = ['Up', 'Left', 'Down', 'Right']
    idx = directions.index(previous_direction)

    new_direction = previous_direction
    

    if keys[pygame.K_RIGHT]:
        if idx + 1 >= len(directions):
            new_direction = directions[0] 

        else:
            new_direction = directions[idx + 1]

    elif keys[pygame.K_LEFT]:
        new_direction = directions[idx-1]

    return new_direction


# Função para gerar a comida
def generate_random_food(square_size, positions):
    return random.choice(positions), random.choice(positions), square_size, square_size       
            

if __name__ == "__main__":
    # Inicializando o pygame
    pygame.init()
    pygame.font.init()

    # Inicializando a tela 
    screen = pygame.display.set_mode([600, 600])
    pygame.display.set_caption("Jogo da cobra")

    # cores
    black = (0,0,0)
    red = (255,0,0)
    white = (255,255,255)

    # Cor da cobra
    green = (0,255,0)
    
    #Inicializando variáveis
    sair = False
    gameover = False
    direction = 'Right'

    square_size = 20
    positions = [i for i in range(600) if i%20 == 0]
    pos_y, pos_x = random.choice(positions), random.choice(positions)

    snake = Snake(pos_y, pos_x)
    fruit_pos = generate_random_food(square_size, positions)
    points = 0
    
    # Fontes
    fontsys = pygame.font.SysFont(pygame.font.get_default_font(), 16)
    fontsys_gameover = pygame.font.SysFont(pygame.font.get_default_font(), 60)

    txt_gameover = fontsys_gameover.render('GAME OVER', 1, white)

    # Looping principal
    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

        if not gameover:
            screen.fill(black)
            for pos in snake.parts_pos:
                pygame.draw.rect(screen, green, (pos[0], pos[1], square_size, square_size))

            pygame.draw.rect(screen, red, (fruit_pos)) 
            txtscreen = fontsys.render(f'Score: {points}', 1, white)
            screen.blit(txtscreen, (520, 520))
            pygame.display.update()

            match direction:
                case 'Right':
                    pos_x += 20

                case 'Left':
                    pos_x -= 20

                case 'Up':
                    pos_y += 20

                case 'Down':
                    pos_y -= 20

            direction = set_direction(direction)
            pos_x_food, pos_y_food = fruit_pos[0], fruit_pos[1]
            position = snake.parts_pos[0]


            if position == (pos_x_food, pos_y_food):
                points += 1
                snake.forward((pos_x, pos_y), grow=True)
                fruit_pos = generate_random_food(square_size=square_size, positions=positions)
            
            elif position[0] not in range(601) or position[1] not in range(601) or position in snake.parts_pos[1:] and len(snake.parts_pos) > 1:
                gameover = True
                screen.fill(black)
                screen.blit(txt_gameover, (180, 250))
            
            elif position != (pos_x_food, pos_y_food):
                snake.forward((pos_x, pos_y), grow=False)

            pygame.display.flip()
            time.sleep(0.15)

    pygame.quit()