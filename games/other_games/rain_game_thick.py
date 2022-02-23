import pygame
import random
import sys

pygame.init()

running = True
while running:

    width = 400
    height = 600

    player_color = (255,255,255)
    enemy_color = (255,255,0)
    score_color = (255,255,255)
    background_color = (0,0,100)
    
    player_size = 50
    player_pos = [width/2, height-player_size]

    enemy_size = 50
    enemy_pos = [random.randint(0,8)*50, 0]
    enemy_list = [enemy_pos]

    score = 0
    speed_rate = 10
    speed = (score//speed_rate)+5

    screen = pygame.display.set_mode((width, height))

    game_over = False



    clock = pygame.time.Clock()

    myFont = pygame.font.SysFont("times new roman", 40)


    def drop_enemies(enemy_list):
            delay = random.random()
            if len(enemy_list) < 10 and delay < 0.1+0.1*score:
                    x_pos = random.randint(0,8)*50
                    y_pos = 0-enemy_size
                    enemy_list.append([x_pos, y_pos])

    def draw_enemies(enemy_list):
            for enemy_pos in enemy_list:
                    pygame.draw.rect(screen, enemy_color, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    def update_enemy_positions(enemy_list, score):
            for idx, enemy_pos in enumerate(enemy_list):
                    if enemy_pos[1] >= 0-enemy_size and enemy_pos[1] < height:
                            enemy_pos[1] += speed
                    else:
                            enemy_list.pop(idx)
                            score += 1
            return score

    def collision_check(enemy_list, player_pos):
            for enemy_pos in enemy_list:
                    if detect_collision(enemy_pos, player_pos):
                            return True
            return False

    def detect_collision(player_pos, enemy_pos):
            p_x = player_pos[0]
            p_y = player_pos[1]

            e_x = enemy_pos[0]
            e_y = enemy_pos[1]

            if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
                    if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
                            return True
            return False

    while not game_over:
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT: #keeps the screen alive until the 'x' button is pressed
                    sys.exit()

                elif event.type == pygame.KEYDOWN:

                        x = player_pos[0]
                        y = player_pos[1]

                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                                x -= player_size
                                if x < 0:
                                    x = 0
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                                x += player_size
                                if x >= width:
                                    x = width-player_size

                        player_pos = [x,y]

            screen.fill(background_color)

            drop_enemies(enemy_list)
            score = update_enemy_positions(enemy_list, score)
            speed = (score//speed_rate)+5

            if collision_check(enemy_list, player_pos):
                    game_over = True
                    

            draw_enemies(enemy_list)

            text = "Score:" + str(score)
            label = myFont.render(text, 1, score_color, background_color)
            screen.blit(label, (0, 0))

            pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))
            
            clock.tick(60)

            pygame.display.update()
            
    while game_over:

        if event.type == pygame.QUIT: #keeps the screen alive until the 'x' button is pressed
                sys.exit()
        
        background_color = (0,0,50)
        screen.fill(background_color)

        speed = 0

        enemy_color = (200,200,0)
        draw_enemies(enemy_list)

        score = update_enemy_positions(enemy_list, score)
        text = "Score:" + str(score)
        label = myFont.render(text, 1, score_color, background_color)
        screen.blit(label, (0, 0))
        
        player_color = (255,0,0)
        pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r or event.key == pygame.K_RETURN:
                    game_over = False
                    pygame.time.delay(500)