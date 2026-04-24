import pygame
import time
import random

# --- ИНИЦИАЛИЗАЦИЯ ---
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 600, 400
SNAKE_BLOCK = 20 # Размер клетки (сетки)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Practice 11: Ultimate Edition')

clock = pygame.time.Clock()

# Цвета (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
YELLOW = (255, 255, 10) # Легкая еда
ORANGE = (255, 165, 0) # Тяжелая еда
BLUE = (50, 153, 213)

# Шрифты
score_font = pygame.font.SysFont("comicsansms", 35)
msg_font = pygame.font.SysFont("bahnschrift", 25)

# --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---

def show_score(score):
    """Выводит счет в левый верхний угол"""
    value = score_font.render(f"Score: {score}", True, BLUE)
    screen.blit(value, [0, 0])

def draw_snake(snake_list):
    """Рисует каждый сегмент змейки"""
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], SNAKE_BLOCK, SNAKE_BLOCK])

def get_food():
    """Создает еду: координаты + рандомный вес (Задание 1)"""
    weight = random.choice([1, 3])
    # Генерируем координаты кратно размеру блока (SNAKE_BLOCK), чтобы змея попадала в еду
    fx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
    fy = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0
    return fx, fy, weight

# --- ОСНОВНОЙ ИГРОВОЙ ЦИКЛ ---

def gameLoop():
    game_over = False  # Флаг полного выхода из игры
    game_close = False # Флаг экрана "Game Over"

    # Начальные координаты головы
    x1, y1 = WIDTH / 2, HEIGHT / 2
    # Вектор движения (в начале стоим)
    dx, dy = 0, 0

    snake_list = []
    snake_length = 1
    score = 0

    # ЗАДАНИЕ 2: Таймер исчезновения еды
    # Создаем свое событие и ставим его на каждые 5000 мс (5 сек)
    FOOD_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(FOOD_EVENT, 5000)

    food_x, food_y, food_w = get_food()

    while not game_over:

        # ЭКРАН ПРОИГРЫША (Game Over Screen)
        while game_close:
            screen.fill(BLACK)
            msg = msg_font.render("Ты проиграл! Q - Выход, C - Заново", True, RED)
            screen.blit(msg, [WIDTH / 6, HEIGHT / 3])
            show_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop() # Рестарт

        # ОБРАБОТКА СОБЫТИЙ (Управление и Таймеры)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            # Если 5 секунд прошло — еда исчезает и появляется в другом месте
            if event.type == FOOD_EVENT:
                food_x, food_y, food_w = get_food()

            if event.type == pygame.KEYDOWN:
                # Управление WASD + защита от движения в противоположную сторону
                if event.key == pygame.K_a and dx == 0:
                    dx, dy = -SNAKE_BLOCK, 0
                elif event.key == pygame.K_d and dx == 0:
                    dx, dy = SNAKE_BLOCK, 0
                elif event.key == pygame.K_w and dy == 0:
                    dx, dy = 0, -SNAKE_BLOCK
                elif event.key == pygame.K_s and dy == 0:
                    dx, dy = 0, SNAKE_BLOCK

        # ПРОВЕРКА ГРАНИЦ (Collision with boundaries)
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # Движение головы
        x1 += dx
        y1 += dy
        screen.fill(BLACK)

        # Рисуем еду (цвет зависит от веса)
        food_color = YELLOW if food_w == 1 else ORANGE
        pygame.draw.rect(screen, food_color, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        # Обновление тела змейки
        head = [x1, y1]
        snake_list.append(head)
        
        # Если список координат длиннее, чем положено змее — удаляем "хвост"
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Проверка: не врезались ли в свой хвост?
        for segment in snake_list[:-1]:
            if segment == head:
                game_close = True

        draw_snake(snake_list)
        show_score(score)

        pygame.display.update()

        # ПРОВЕРКА: СЪЕЛИ ЕДУ?
        if x1 == food_x and y1 == food_y:
            score += food_w
            snake_length += food_w # Растем на вес еды (Задание 1)
            food_x, food_y, food_w = get_food()
            # Сбрасываем таймер еды, чтобы новое яблоко не исчезло сразу
            pygame.time.set_timer(FOOD_EVENT, 5000)

        # Скорость игры
        clock.tick(12)

    pygame.quit()
    exit()

# Запуск игры
gameLoop()
