import pygame
import time
import random

# 1. Инициализируем всё (включаем движок)
pygame.init()

# Настройки цветов (RGB - Red, Green, Blue от 0 до 255)
WHITE = (255, 255, 255)  # Все цвета на максимум = белый
YELLOW = (255, 255, 102) # Желтая еда
BLACK = (0, 0, 0)       # Тишина и пустота = черный фон
RED = (213, 50, 80)     # Красный для надписи "Проиграл"
GREEN = (0, 255, 0)     # Чистый зеленый для змеи
BLUE = (50, 153, 213)   # Голубой для циферок счета

# Размер окна
DIS_WIDTH = 600
DIS_HEIGHT = 400
# Создаем само окошко
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game: Advanced Level')

# Это наш менеджер времени. Без него змейка улетит в космос за секунду
clock = pygame.time.Clock() 

SNAKE_BLOCK = 10   # Размер одного "зерна" змейки (сетка 10x10)
initial_speed = 10 # Сколько кадров (клеток) в секунду проходим в начале

# Подключаем шрифты (название, размер)
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# --- ФУНКЦИИ ПОМОЩНИКИ (Чтобы не загромождать основной цикл) ---

def our_snake(snake_block, snake_list):
    """Рисуем змейку. snake_list - это список всех координат тела [(x1,y1), (x2,y2)...]"""
    for x in snake_list:
        # Рисуем квадратик для каждой координаты в списке
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """Штука для вывода текста. Render превращает буквы в картинку, blit клеит её на экран"""
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [DIS_WIDTH / 6, DIS_HEIGHT / 3]) # Чуть левее центра и чуть выше середины

def display_score(score, level):
    """Рисуем счет слева, уровень справа. str() нужен, чтобы склеить текст с числом"""
    value = score_font.render("Score: " + str(score), True, BLUE)
    lvl = score_font.render("Level: " + str(level), True, BLUE)
    dis.blit(value, [0, 0]) # В самый верхний левый угол
    dis.blit(lvl, [DIS_WIDTH - 150, 0]) # В правый угол (отступив 150 пикселей)

# --- ГЛАВНАЯ ЛОГИКА ИГРЫ ---

def gameLoop():
    # Флаги состояний
    game_over = False  # Когда совсем закрыли окно
    game_close = False # Когда врезались, но есть шанс нажать "C" (начать заново)

    # Стартуем из середины
    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2

    # Изменение координат. Если 0 - стоим и ждем нажатия
    x1_change = 0
    y1_change = 0

    snake_List = []      # Список всех "кусочков" тела
    Length_of_snake = 1  # Текущая длина (в начале только голова)
    
    score = 0
    level = 1
    current_speed = initial_speed

    # Вложенная функция для еды
    def generate_food(snake_list):
        """Создаем еду так, чтобы она попала в сетку 10x10 и не на змею"""
        while True:
            # Магия математики: выбираем число, делим на 10, округляем и умножаем на 10. 
            # Так еда всегда будет стоять ровно в клеточке змейки (например, 140, а не 143)
            foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            # Если эти координаты не заняты телом змеи - отдаем их!
            if [foodx, foody] not in snake_list:
                return foodx, foody

    # Создаем первую порцию еды
    foodx, foody = generate_food(snake_List)

    # ГЛАВНЫЙ ЦИКЛ (жизнь игры)
    while not game_over:

        # ЭКРАН СМЕРТИ (зациклен, пока игрок не выберет Q или C)
        while game_close == True:
            dis.fill(BLACK)
            message("Ты проиграл! Q-Выход или C-Играть снова", RED)
            display_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: # Quit
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: # Continue
                        gameLoop() # Рекурсия: запускаем функцию заново

        # СЛУШАЕМ КЛАВИАТУРУ
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # Проверка `change == 0` нужна, чтобы змея не могла развернуться на 180 градусов в себя
                if event.key == pygame.K_a and x1_change == 0: # Влево
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_d and x1_change == 0: # Вправо
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_w and y1_change == 0: # Вверх
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_s and y1_change == 0: # Вниз
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        # ПРОВЕРКА ГРАНИЦ: если голова вышла за рамки экрана - Game Over
        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True
        
        # Обновляем координаты головы
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK) # Сначала заливаем всё черным (стираем прошлый кадр)

        # Рисуем еду
        pygame.draw.rect(dis, YELLOW, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        
        # ДВИЖЕНИЕ ХВОСТА
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head) # Добавляем новую голову в список тела
        
        # Если список координат длиннее, чем положено змее, удаляем самый старый (хвост)
        # Так получается эффект движения: спереди добавили, сзади отрезали
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # САМОПОЕДАНИЕ: если координаты новой головы уже есть в списке тела - мы врезались
        for x in snake_List[:-1]: # Проверяем всё тело, кроме самой головы
            if x == snake_Head:
                game_close = True

        # Вызываем наших помощников, чтобы всё отрисовать
        our_snake(SNAKE_BLOCK, snake_List)
        display_score(score, level)

        # Наконец, показываем всё это на мониторе
        pygame.display.update()

        # ОБЕД: если голова наступила на еду
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food(snake_List) # Новая еда
            Length_of_snake += 1 # Растем
            score += 1
            
            # СИСТЕМА УРОВНЕЙ: каждые 3 очка змея становится быстрее
            # % - это остаток от деления. Если score % 3 == 0, значит число делится на 3 без остатка
            if score % 3 == 0:
                level += 1
                current_speed += 3 # +3 к сложности!

        # Ждем немного до следующего кадра (контроль скорости)
        clock.tick(current_speed)

    # Если вышли из цикла - всё выключаем
    pygame.quit()
    quit()

# Поехали!
gameLoop()