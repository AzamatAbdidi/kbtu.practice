import pygame
import random
import time
import os # Чтобы комп сам находил файлы по путям

# --- ИНИЦИАЛИЗАЦИЯ ---
pygame.init()
pygame.mixer.init() # Включаем звук

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Practice 11")
timer = pygame.time.Clock()

# Цвета
WHITE, RED, BLACK, YELLOW = (255, 255, 255), (255, 0, 0), (0, 0, 0), (255, 255, 0)
GOLD = (218, 165, 32) 

# Переменные (состояние игры)
speed = 5
score = 0
coins_collected = 0

# Шрифты
font_small = pygame.font.SysFont("Verdana", 20)

# --- ЗАГРУЗКА ЗВУКОВ ---
# Находим путь к папке, где лежит наш скрипт
current_path = os.path.dirname(__file__)
# Соединяем путь с папкой sounds (убедись, что она есть в Practice11/racer/)
sounds_path = os.path.join(current_path, "sounds")

try:
    # 1. Фоновая музыка (Tokyo Drift)
    pygame.mixer.music.load(os.path.join(sounds_path, "51745-tokyo-drift-teriyaki-boyz5.mp3"))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1) # Зацикливаем

    # 2. Эффекты
    coin_sound = pygame.mixer.Sound(os.path.join(sounds_path, "s1_a0.mp3"))
    crash_sound = pygame.mixer.Sound(os.path.join(sounds_path, "s1_a2.mp3"))
except Exception as e:
    print(f"Ошибка загрузки звуков: {e}")
    # Если звуков нет, создаем "пустышки", чтобы игра не ломалась
    coin_sound = pygame.mixer.Sound(pygame.Surface((0,0)))
    crash_sound = pygame.mixer.Sound(pygame.Surface((0,0)))

# --- КЛАССЫ ОБЪЕКТОВ ---

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # ЗАДАНИЕ 1: Рандомный вес монетки (1 или 5)
        self.weight = random.choice([1, 5]) 
        self.image = pygame.Surface((30, 30))
        self.image.set_colorkey(BLACK)
        
        # Тяжелые монетки делаем золотыми, обычные - желтыми
        color = GOLD if self.weight == 5 else YELLOW
        pygame.draw.circle(self.image, color, (15, 15), 15)
        
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), -50)

    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.top > HEIGHT:
            self.__init__() # Респаун и рандом нового веса

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), -100)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > HEIGHT:
            score += 1 # Считаем, сколько машин пропустили
            self.rect.top = -100
            self.rect.center = (random.randint(40, WIDTH-40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((44, 80))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 0 and keys[pygame.K_LEFT]: self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH and keys[pygame.K_RIGHT]: self.rect.move_ip(5, 0)

# --- СОЗДАНИЕ ОБЪЕКТОВ ---
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group(E1)
all_coins = pygame.sprite.Group(C1)
all_sprites = pygame.sprite.Group(P1, E1, C1)

# --- ГЛАВНЫЙ ЦИКЛ ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); exit()

    screen.fill(WHITE)
    
    # Рисуем счетчики (верхние углы)
    screen.blit(font_small.render(f"Score: {score}", True, BLACK), (10, 10))
    screen.blit(font_small.render(f"Coins: {coins_collected}", True, BLACK), (280, 10))

    # Двигаем всё и рисуем
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)
        sprite.move()

    # СБОР МОНЕТ (Задания 1 и 2)
    collected = pygame.sprite.spritecollide(P1, all_coins, False)
    for coin in collected:
        coin_sound.play() # Звук монетки!
        
        old_coins = coins_collected
        coins_collected += coin.weight # Добавляем вес (1 или 5)
        
        # ЗАДАНИЕ 2: Ускорение врага каждые 10 собранных монет (N = 10)
        # Проверяем, перешагнули ли мы порог в десяток
        if (coins_collected // 10) > (old_coins // 10):
            speed += 1 
            print(f"СКОРОСТЬ УВЕЛИЧЕНА! Текущая: {speed}")
            
        coin.__init__() # Сбрасываем монетку наверх с новым весом

    # СТОЛКНОВЕНИЕ С ВРАГОМ (ФЕЙЛ)
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop() # Тишина...
        crash_sound.play() # БАБАХ!
        
        screen.fill(RED)
        msg = pygame.font.SysFont("Verdana", 60).render("GAME OVER", True, BLACK)
        screen.blit(msg, (30, 250))
        pygame.display.update()
        
        time.sleep(2) # Пауза для драматизма
        pygame.quit(); exit()

    pygame.display.update()
    timer.tick(60)