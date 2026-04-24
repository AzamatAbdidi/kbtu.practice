import pygame

# --- ИНИЦИАЛИЗАЦИЯ (ПОДГОТОВКА) ---
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Professional Paint v1.0")

clock = pygame.time.Clock()

# Константы цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# CANVAS (Холст) - это отдельная поверхность (Surface). 
# Профи-совет: мы рисуем на холсте, а холст потом "накладываем" на экран. 
# Это нужно, чтобы интерфейс (кнопки) не затирался рисунком.
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(BLACK)

# Палитра - список кортежей (кортеж - это неизменяемый список)
palette = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 165, 0), (255, 255, 255)
]

# Глобальные стейты (состояния) программы
color = (0, 0, 255) # Текущий цвет (по умолчанию синий)
tool = 'brush'      # Активный инструмент
radius = 10         # Радиус кисти/ластика
drawing = False     # Флаг: нажал ли юзер кнопку мыши прямо сейчас?
start_pos = (0, 0)  # Координата начала рисования (нужна для фигур)

font = pygame.font.SysFont("Arial", 20)

# --- ГЛАВНЫЙ ЦИКЛ ОБРАБОТКИ СОБЫТИЙ ---
while True:
    # event.get() выгребает "очередь событий" (нажатия, движения мыши)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # ОБРАБОТКА КЛАВИАТУРЫ (Смена инструментов)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: tool = 'brush'
            if event.key == pygame.K_2: tool = 'rect'
            if event.key == pygame.K_3: tool = 'circle'
            if event.key == pygame.K_4: tool = 'eraser'

        # ОБРАБОТКА МЫШИ (Нажали кнопку)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # ПРОВЕРКА ПАЛИТРЫ (Коллизия курсора с кнопками цветов)
            # Перебираем все квадратики цветов
            for i, c in enumerate(palette):
                # Если X и Y мыши попали в границы квадрата палитры
                if 10 + i*50 <= x <= 50 + i*50 and 10 <= y <= 50:
                    color = c

            if event.button == 1: # 1 - это левая кнопка мыши (ЛКМ)
                drawing = True
                start_pos = event.pos # Запоминаем "якорь" для фигур

            # Регулировка размера кисти через правую кнопку (ПКМ)
            elif event.button == 3: 
                radius = radius + 2 if radius < 50 else 2 # Зацикленный размер

        # ОБРАБОТКА МЫШИ (Отпустили кнопку)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos

                # ГЕОМЕТРИЧЕСКИЙ РАСЧЕТ ДЛЯ ФИГУР
                # Эти фигуры рисуются один раз в момент отпускания мыши
                if tool == 'rect':
                    # Вычисляем верхний левый угол (через min) и ширину/высоту (через abs)
                    # Это позволяет рисовать прямоугольник в любую сторону
                    rect_x = min(start_pos[0], end_pos[0])
                    rect_y = min(start_pos[1], end_pos[1])
                    width = abs(start_pos[0] - end_pos[0])
                    height = abs(start_pos[1] - end_pos[1])
                    pygame.draw.rect(canvas, color, (rect_x, rect_y, width, height), 2)

                elif tool == 'circle':
                    # Теорема Пифагора для нахождения радиуса: R = sqrt((x2-x1)^2 + (y2-y1)^2)
                    dx = start_pos[0] - end_pos[0]
                    dy = start_pos[1] - end_pos[1]
                    dist = int((dx**2 + dy**2)**0.5)
                    pygame.draw.circle(canvas, color, start_pos, dist, 2)

        # ОБРАБОТКА МЫШИ (Движение)
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                # Инструменты непрерывного рисования
                if tool == 'brush':
                    # Рисуем круги на каждом кадре движения. 
                    # Профи-тема: если вести мышь быстро, будут "дырки". 
                    # В идеале тут рисуют линию между прошлой и текущей позицией.
                    pygame.draw.circle(canvas, color, event.pos, radius)

                elif tool == 'eraser':
                    # Ластик - это просто кисть, которая красит в цвет фона (BLACK)
                    pygame.draw.circle(canvas, BLACK, event.pos, radius)

    # --- ОТРЕСОВКА (РЕНДЕРИНГ) ---
    
    # 1. Сначала чистим основной экран
    screen.fill(BLACK)
    
    # 2. Отрисовываем наш холст (canvas) со всеми рисунками
    screen.blit(canvas, (0, 0))

    # 3. Отрисовываем UI (Интерфейс) поверх холста
    # Рисуем квадраты палитры
    for i, c in enumerate(palette):
        # Рисуем обводку для активного цвета
        if c == color:
            pygame.draw.rect(screen, WHITE, (8 + i*50, 8, 44, 44), 2)
        pygame.draw.rect(screen, c, (10 + i*50, 10, 40, 40))

    # Вывод текста (состояние программы)
    info_text = f"Tool: {tool.upper()} | Size: {radius} | Color: {color}"
    text_surf = font.render(info_text, True, WHITE)
    screen.blit(text_surf, (10, 60))

    # Обновляем кадр и держим 60 FPS
    pygame.display.flip()
    clock.tick(60)