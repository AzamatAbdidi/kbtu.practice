import pygame # Подтягиваем сам движок, без него ниче не будет
import random # Это чтобы враги и монетки спавнились где попало, а не в одной точке
import time   # Нужен, чтобы игра не закрывалась мгновенно после проигрыша
import os     # Мега-важная штука, чтобы комп сам нашел музыку в папках

# --- ЭТАП 1: ВКЛЮЧАЕМ ВСЁ ---
pygame.init()       # Сказали компу: "Эй, мы будем рисовать графику"
pygame.mixer.init() # Сказали компу: "И звук тоже будет, готовь колонки"

# --- ЭТАП 2: НАСТРОЙКИ ЭКРАНА (ТЕЛЕВИЗОР) ---
WIDTH = 400  # Ширина нашего окна в пикселях
HEIGHT = 600 # Высота окна. Оно будет вертикальным, как на телефоне
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Создаем само окно
pygame.display.set_caption("Tokyo Drift Racer") # Название игры в шапке окна
timer = pygame.time.Clock() # Эта штука будет следить, чтобы игра не летала слишком быстро

# --- ЭТАП 3: ЦВЕТОВАЯ ПАЛИТРА ---
# Числа - это RGB (Red, Green, Blue). От 0 до 255.
WHITE = (255, 255, 255) # Максимум всего = белый
RED = (255, 0, 0)       # Только красный
BLACK = (0, 0, 0)       # Тишина и пустота = черный
YELLOW = (255, 255, 0)  # Красный + зеленый = желтый (для монет)

# --- ЭТАП 4: ТЕКСТ (ШРИФТЫ) ---
# "Verdana" - это название шрифта, цифры - размер букв
font_small = pygame.font.SysFont("Verdana", 20) # Для счетчика очков
font_big = pygame.font.SysFont("Verdana", 60)   # Для надписи "Ты проиграл"

# --- ЭТАП 5: ИГРОВЫЕ ПЕРЕМЕННЫЕ (ЦИФЕРКИ) ---
speed = 5 # С этой скоростью всё падает вниз. Чем больше число, тем сложнее
score = 0 # Сколько машин мы объехали
coins = 0 # Сколько бабок насобирали

# --- ЭТАП 6: МУЗОН (САМОЕ СЛОЖНОЕ С ПУТЯМИ) ---
# os.path.dirname(__file__) говорит: "Найди папку, где лежит этот мой файл .py"
current_path = os.path.dirname(__file__) 
# Соединяем путь к папке и папку sounds. Теперь комп точно не потеряется.
sounds_path = os.path.join(current_path, "sounds")

try: # "try" значит "попробуй сделать это, но если файлов нет - не взрывайся"
    # Фоновая музыка (load - загрузить)
    pygame.mixer.music.load(os.path.join(sounds_path, "51745-tokyo-drift-teriyaki-boyz5.mp3"))
    pygame.mixer.music.set_volume(0.3) # Громкость на 30%, чтобы мама не пришла ругаться
    pygame.mixer.music.play(-1) # -1 значит играть бесконечно по кругу

    # Эффекты (Sound - для коротких "пшиков")
    coin_sound = pygame.mixer.Sound(os.path.join(sounds_path, "s1_a0.mp3"))
    crash_sound = pygame.mixer.Sound(os.path.join(sounds_path, "s1_a2.mp3"))
except Exception as e: # Если музона нет, выводим ошибку в консоль
    print(f"Бро, музон не качает! Ошибка: {e}")
    # Делаем фейковые пустые звуки, чтобы код не выдал ошибку при вызове play()
    coin_sound = pygame.mixer.Sound(pygame.Surface((0,0))) 
    crash_sound = pygame.mixer.Sound(pygame.Surface((0,0)))

# --- ЭТАП 7: КЛАССЫ (ЧЕРТЕЖИ ОБЪЕКТОВ) ---

# Монетка
class Coin(pygame.sprite.Sprite): # Sprite - это стандартный "актер" в pygame
    def __init__(self): # Это запускается один раз при создании монетки
        super().__init__() # Магия, чтобы спрайт работал правильно
        self.image = pygame.Surface((30, 30)) # Делаем квадрат 30 на 30 пикселей
        self.image.set_colorkey(BLACK) # Делаем черный цвет прозрачным
        pygame.draw.circle(self.image, YELLOW, (15, 15), 15) # Рисуем желтый круг внутри квадрата
        self.rect = self.image.get_rect() # Это невидимая рамка вокруг круга для столкновений
        # Ставим монетку в случайное место по горизонтали и чуть выше экрана (-100)
        self.rect.center = (random.randint(40, WIDTH-40), random.randint(-100, 0))

    def move(self): # Что монетка делает каждый кадр
        self.rect.move_ip(0, speed) # Двигается вниз (по оси Y) на значение speed
        if (self.rect.top > HEIGHT): # Если улетела за нижний край экрана
            self.rect.top = 0 # Возвращаем наверх
            self.rect.center = (random.randint(40, WIDTH-40), 0) # Опять в рандомное место

# Враг (красный квадрат)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 80)) # Прямоугольник как машина
        self.image.fill(RED) # Красим в красный (опасно!)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), 0)

    def move(self):
        global score # Берем ту самую переменную score, что была в начале
        self.rect.move_ip(0, speed)
        if (self.rect.top > HEIGHT): # Если объехали врага
            score += 1 # Красава, лови очко
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH-40), 0)

# Игрок (черный квадрат)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((44, 80))
        self.image.fill(BLACK) # Наша тачка - черная
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) # Начальная позиция внизу экрана

    def move(self):
        keys = pygame.key.get_pressed() # Слушаем, че там нажимает юзер
        # Если нажата стрелка влево и мы не уперлись в левый край (0)
        if self.rect.left > 0 and keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0) # Двигаем влево на 5 пикселей
        # Если нажата вправо и мы не вылетели за правую границу (WIDTH)
        if self.rect.right < WIDTH and keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0) # Двигаем вправо

# --- ЭТАП 8: СОЗДАЕМ И ГРУППИРУЕМ ---
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Создаем группы. Это как папки, чтобы проверять столкновения сразу со всеми внутри
enemies = pygame.sprite.Group()
enemies.add(E1)

all_coins = pygame.sprite.Group()
all_coins.add(C1)

# Группа для отрисовки - тут вообще все
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# --- ЭТАП 9: ГЛАВНЫЙ ЦИКЛ (БЕСКОНЕЧНОСТЬ) ---
while True:
    # 1. Проверяем, не хочет ли юзер выйти
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Вырубаем pygame
            exit() # Вырубаем саму программу

    screen.fill(WHITE) # Каждый кадр красим всё в белый, чтобы стереть старые следы
    
    # 2. Пишем текст на экране (f-строки - это магия для вставки переменных в текст)
    scores_txt = font_small.render(f"Score: {score}", True, BLACK)
    coins_txt = font_small.render(f"Coins: {coins}", True, BLACK)
    screen.blit(scores_txt, (10, 10))   # Левый верхний угол
    screen.blit(coins_txt, (300, 10)) # Правый верхний угол

    # 3. Двигаем и рисуем всё, что есть в группе all_sprites
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect) # Рисуем картинку на её позиции
        sprite.move() # Вызываем метод move, который мы написали в классах

    # 4. ПРОВЕРКА МОНЕТОК (БЕРЕМ БАБЛО)
    # spritecollide ищет касания игрока (P1) и группы монет
    # False в конце значит "не удаляй объект из памяти"
    collected_coins = pygame.sprite.spritecollide(P1, all_coins, False)
    for coin in collected_coins:
        coin_sound.play() # Дзынь!
        coins += 1 # Счётчик бабла растёт
        # Кидаем монетку за экран наверх, чтобы она "переродилась"
        coin.rect.top = -100 
        coin.rect.center = (random.randint(40, WIDTH-40), 0)

    # 5. ПРОВЕРКА СМЕРТИ (ДТП)
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop() # Глушим Токио Дрифт, пора грустить
        crash_sound.play() # Звук удара
        
        screen.fill(RED) # Заливаем всё красным
        msg = font_big.render("GAME OVER", True, BLACK)
        screen.blit(msg, (30, 250)) # Рисуем надпись по центру
        pygame.display.update() # Срочно обновляем экран, чтобы юзер увидел смерть
        
        time.sleep(2) # Замираем на 2 секунды, чтобы осознать фиаско
        pygame.quit() # Всё, расходимся
        exit()

    # 6. ОБНОВЛЕНИЕ КАДРА
    pygame.display.update() # Показываем всё, что нарисовали выше
    timer.tick(60) # Делаем ровно 60 кадров в секунду (как в топовых играх)