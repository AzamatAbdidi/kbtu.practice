import pygame
import datetime

# 1. Инициализация Pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")
clock = pygame.time.Clock()

# 2. Загрузка изображений
# Убедись, что названия файлов в папке images совпадают!
try:
    bg_image = pygame.image.load('mickeys_clock/images/main-clock.png').convert_alpha()
    min_hand_img = pygame.image.load('mickeys_clock/images/left-hand.png').convert_alpha()
    sec_hand_img = pygame.image.load('mickeys_clock/images/right-hand.png').convert_alpha()
except FileNotFoundError:
    print("Ошибка: Не найдены файлы в папке images. Проверь пути!")
    pygame.quit()
    exit()

def blit_rotate_center(surf, image, center, angle):
    """Функция для вращения картинки вокруг центра экрана"""
    # Вращаем саму картинку
    rotated_image = pygame.transform.rotate(image, angle)
    # Определяем новый прямоугольник с сохранением центра
    new_rect = rotated_image.get_rect(center=image.get_rect(center=center).center)
    surf.blit(rotated_image, new_rect)

running = True
while running:
    # 3. Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 4. Логика времени
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    # Расчет углов:
    # 1 секунда = 6 градусов (360/60)
    # Мы ставим минус, чтобы вращение было по часовой стрелке
    # Если руки на исходной картинке смотрят не на 12 часов, добавь смещение (например +90)
    angle_sec = -seconds * 6 
    angle_min = -minutes * 6

    # 5. Отрисовка
    screen.fill((255, 255, 255)) # Чистим экран белым фоном
    
    # Рисуем циферблат (он должен быть 800x800 или отцентрован)
    bg_rect = bg_image.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(bg_image, bg_rect)

    # Рисуем руки Микки
    # (WIDTH//2, HEIGHT//2) — это точка, вокруг которой всё крутится
    blit_rotate_center(screen, min_hand_img, (WIDTH//2, HEIGHT//2), angle_min)
    blit_rotate_center(screen, sec_hand_img, (WIDTH//2, HEIGHT//2), angle_sec)

    pygame.display.flip() # Обновляем кадр
    clock.tick(60) # Ограничение до 60 FPS

pygame.quit()