import pygame
import time
import random

# Инициализируем всё (включаем движок)
pygame.init()

# Настройки цветов (RGB)
WHITE = (255, 255, 255) # Белый
YELLOW = (255, 255, 102) # Желтый (для еды)
BLACK = (0, 0, 0)       # Черный (для фона)
RED = (213, 50, 80)     # Красный (для сообщений)
GREEN = (0, 255, 0)     # Зеленый (для змейки)
BLUE = (50, 153, 213)   # Голубой (для текста счета)

# Размер окна (делаем квадратным, так проще считать сетку)
DIS_WIDTH = 600
DIS_HEIGHT = 400
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game: Advanced Level')

clock = pygame.time.Clock() # Таймер для скорости

SNAKE_BLOCK = 10 # Размер одного квадратика змейки
initial_speed = 10 # Начальная скорость

# Шрифты для текста
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# --- ФУНКЦИИ ПОМОЩНИКИ ---

def our_snake(snake_block, snake_list):
    """Рисуем змейку по списку координат"""
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """Вывод сообщения по центру экрана"""
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [DIS_WIDTH / 6, DIS_HEIGHT / 3])

def display_score(score, level):
    """Показываем счет и уровень (Задание 6)"""
    value = score_font.render("Score: " + str(score), True, BLUE)
    lvl = score_font.render("Level: " + str(level), True, BLUE)
    dis.blit(value, [0, 0])
    dis.blit(lvl, [DIS_WIDTH - 150, 0])

# --- ГЛАВНАЯ ЛОГИКА ---

def gameLoop():
    game_over = False
    game_close = False

    # Начальные координаты головы (центр экрана)
    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2

    # Переменные для движения (в начале стоим на месте)
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    
    score = 0
    level = 1
    current_speed = initial_speed

    # Генерация еды (Задание 2: чтобы не попала на змейку)
    def generate_food(snake_list):
        while True:
            foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            # Проверяем, не попала ли еда внутрь змейки
            if [foodx, foody] not in snake_list:
                return foodx, foody

    foodx, foody = generate_food(snake_List)

    while not game_over:

        # Окно проигрыша
        while game_close == True:
            dis.fill(BLACK)
            message("Ты проиграл! Q-Выход или C-Играть снова", RED)
            display_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Управление кнопками
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_d and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_w and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_s and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        # ПРОВЕРКА ГРАНИЦ (Задание 1)
        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True
        
        # Двигаем голову
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)

        # Рисуем еду
        pygame.draw.rect(dis, YELLOW, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        
        # Логика тела змейки
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # ПРОВЕРКА: врезались ли сами в себя?
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(SNAKE_BLOCK, snake_List)
        display_score(score, level)

        pygame.display.update()

        # ПРОВЕРКА: съели еду?
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food(snake_List)
            Length_of_snake += 1
            score += 1
            
            # ДОБАВЛЕНИЕ УРОВНЕЙ (Задание 3 и 5)
            # Каждые 3 еды — новый уровень и выше скорость
            if score % 3 == 0:
                level += 1
                current_speed += 3 # Ускоряем змейку

        clock.tick(current_speed)

    pygame.quit()
    quit()

gameLoop()