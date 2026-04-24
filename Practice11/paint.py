import pygame
import math # Математика нужна для расчета вершин треугольников

# --- ИНИЦИАЛИЗАЦИЯ ---
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Pro: Geometry Edition (Practice 11)")

# Создаем Surface (холст), чтобы рисунки не исчезали при обновлении экрана
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((0, 0, 0)) # Черный фон холста

clock = pygame.time.Clock()
color = (0, 255, 0) # По умолчанию рисуем зеленым
tool = 'square'      # Стартовый инструмент
drawing = False
start_pos = (0, 0)

# Шрифты для интерфейса
font = pygame.font.SysFont("Verdana", 15)

# Вспомогательная функция для текста
def draw_ui():
    pygame.draw.rect(screen, (50, 50, 50), (0, HEIGHT - 40, WIDTH, 40)) # Панель внизу
    txt = f"Tool: {tool.upper()} | Keys: 1-Square, 2-Right Tri, 3-Equilat Tri, 4-Rhombus | C-Clear"
    ui_surf = font.render(txt, True, (255, 255, 255))
    screen.blit(ui_surf, (10, HEIGHT - 30))

# --- ГЛАВНЫЙ ЦИКЛ ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); exit()

        # ОБРАБОТКА КЛАВИШ (Выбор инструмента)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: tool = 'square'
            if event.key == pygame.K_2: tool = 'right_triangle'
            if event.key == pygame.K_3: tool = 'equilateral_triangle'
            if event.key == pygame.K_4: tool = 'rhombus'
            if event.key == pygame.K_c: canvas.fill((0, 0, 0)) # Очистка экрана

        # НАЖАТИЕ МЫШИ
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # ЛКМ
                drawing = True
                start_pos = event.pos

        # ОТПУСКАНИЕ МЫШИ (Здесь происходит финальная отрисовка фигуры)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos

                # --- ЗАДАНИЯ 1-4: ГЕОМЕТРИЯ ---

                # 1. Квадрат (Square)
                if tool == 'square':
                    # Вычисляем сторону как максимальную разницу, чтобы был именно квадрат
                    side = max(abs(x2 - x1), abs(y2 - y1))
                    # Рисуем по координатам начала (x1, y1)
                    pygame.draw.rect(canvas, color, (x1, y1, side, side), 2)

                # 2. Прямоугольный треугольник (Right Triangle)
                elif tool == 'right_triangle':
                    # Используем polygon для отрисовки по трем точкам
                    # Точки: Начало, конец диагонали и точка прямого угла
                    points = [(x1, y1), (x2, y2), (x1, y2)]
                    pygame.draw.polygon(canvas, color, points, 2)

                # 3. Равносторонний треугольник (Equilateral Triangle)
                elif tool == 'equilateral_triangle':
                    # Длина основания
                    a = x2 - x1
                    # Высота равностороннего треугольника h = a * sin(60°) ≈ a * 0.866
                    h = a * math.sqrt(3) / 2
                    # Точки: две на основании и одна по центру выше/ниже
                    points = [(x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - h)]
                    pygame.draw.polygon(canvas, color, points, 2)

                # 4. Ромб (Rhombus)
                elif tool == 'rhombus':
                    # Находим середины сторон воображаемого прямоугольника
                    mid_x = (x1 + x2) / 2
                    mid_y = (y1 + y2) / 2
                    # Соединяем верх, право, низ и лево
                    points = [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)]
                    pygame.draw.polygon(canvas, color, points, 2)

    # --- РЕНДЕРИНГ ---
    screen.fill((0, 0, 0))
    screen.blit(canvas, (0, 0)) # Отрисовываем холст
    
    # Визуальный "предпросмотр" (опционально, можно добавить для красоты)
    # Но для лабы достаточно отрисовки по MOUSEBUTTONUP

    draw_ui() # Рисуем панель управления сверху

    pygame.display.flip()
    clock.tick(60)