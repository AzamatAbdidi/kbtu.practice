import pygame
import os # эта штука нужна, чтобы комп видел файлы в папке

# Сначала все включаем, без этого ничего не заработает
pygame.init()
pygame.mixer.init() # это специально для звука

# Делаем окошко, чтобы игра не вылетала сразу
# (400, 300) - это просто размер окна, типа маленькое
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Мой плеер") # заголовок окна

# Путь к папке, где лежат мои крутые треки
music_folder = "music_player/music/"

# Создаем пустой список для песен
songs = []

# Чекаем все файлы в папке и добавляем в список только музыку
for file in os.listdir(music_folder):
    if file.endswith(".mp3"): # если файл - музыкалка
        songs.append(file) # кидаем в наш список
    if file.endswith(".wav"): # или если такой формат
        songs.append(file)

# Какая песня играет сейчас? Начинаем с самой первой (это 0 в программировании)
current_song_index = 0

# Функция, чтобы не писать одно и то же 100 раз
def start_music(index):
    # Берем путь к папке + название песни из списка
    path_to_file = os.path.join(music_folder, songs[index])
    pygame.mixer.music.load(path_to_file) # заряжаем трек
    pygame.mixer.music.play() # ПОГНАЛИ!
    print("Сейчас качает: " + songs[index])

# Если в папке реально есть музыка, то врубаем первый трек
if len(songs) > 0:
    start_music(current_song_index)

# Переменные-флаги, чтобы понимать че происходит
game_works = True
is_paused = False

# Главный цикл - тут всё крутится, пока мы не нажмем крестик
while game_works:
    
    # Чекаем, че там юзер нажал на клаве или мышке
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # если нажали на крестик окна
            game_works = False # выходим из цикла
        
        # Если нажата какая-то кнопка на клаве
        if event.type == pygame.KEYDOWN:
            
            # Если нажали P (пауза)
            if event.key == pygame.K_p:
                if is_paused == False: # если музыка играла
                    pygame.mixer.music.pause() # стопаем на время
                    is_paused = True # запоминаем, что мы на паузе
                    print("Тишина...")
                else: # если и так стояла пауза
                    pygame.mixer.music.unpause() # погнали дальше
                    is_paused = False
                    print("Продолжаем флекс!")

            # Если нажали S (стоп)
            if event.key == pygame.K_s:
                pygame.mixer.music.stop() # вырубаем музыку совсем
                print("Выключил нафиг")

            # Если нажали N (следующая / Next)
            if event.key == pygame.K_n:
                current_song_index = current_song_index + 1 # прибавляем 1
                # Если песни кончились, идем в начало списка
                if current_song_index >= len(songs):
                    current_song_index = 0
                start_music(current_song_index)

            # Если нажали B (назад / Back)
            if event.key == pygame.K_b:
                current_song_index = current_song_index - 1 # отнимаем 1
                # Если ушли в минус, прыгаем в самый конец списка
                if current_song_index < 0:
                    current_song_index = len(songs) - 1
                start_music(current_song_index)

    # Просто красим экран в белый, чтобы не было черной пустоты
    screen.fill((255, 255, 255))
    pygame.display.flip() # обновляем картинку

# Когда вышли из цикла - все вырубаем
pygame.quit()
