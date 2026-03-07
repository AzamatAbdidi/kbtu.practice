#1 пример
import os
# Удаление файла "demofile.txt" напрямую
os.remove("demofile.txt")

#2 пример
import os

# Проверяем, существует ли файл по указанному пути
if os.path.exists("demofile.txt"):
    # Если существует, удаляем его
    os.remove("demofile.txt")
else:
    # Если файла нет, выводим сообщение
    print("Файл не существует")


#3 пример
import os

# Удаление папки с именем "myfolder"
os.rmdir("myfolder")

# Примечание: Вы можете удалять только ПУСТЫЕ папки.
# Если в папке есть файлы, возникнет ошибка.