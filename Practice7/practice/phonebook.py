import psycopg2
import csv
from config import load_config

def create_table():
    # Создание таблицы в PostgreSQL 
    sql = """
    CREATE TABLE IF NOT EXISTS phonebook (
        contact_id SERIAL PRIMARY KEY,
        contact_name VARCHAR(500) NOT NULL,
        phone_number VARCHAR(500) NOT NULL UNIQUE
    )
    """
    conn = None
    try:
        params = load_config()
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # Выполняем SQL-запрос
                cur.execute(sql)
                print("Таблица 'phonebook' успешно создана или уже существует.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка при создании таблицы: {error}")

def insert_contact(name, phone):
    """ Вставка нового контакта в таблицу phonebook """
    sql = """INSERT INTO phonebook(contact_name, phone_number)
             VALUES(%s, %s) RETURNING contact_id;"""
    conn = None
    contact_id = None
    try:
        params = load_config()
        # Используем конструкцию with, чтобы соединение закрылось само
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # Выполняем команду. %s — это безопасные "заглушки" для данных
                cur.execute(sql, (name, phone))
                
                # Получаем ID новой записи
                contact_id = cur.fetchone()[0]
                
                # ВАЖНО: фиксируем изменения в базе
                conn.commit()
                print(f"Контакт '{name}' успешно добавлен с ID: {contact_id}")
                
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка при добавлении контакта: {error}")
    
    return contact_id

def insert_from_csv(file_path):
    """ Загрузка контактов из CSV-файла в базу данных """
    # Добавил ON CONFLICT DO NOTHING, чтобы не было ошибок при повторном запуске
    sql = "INSERT INTO phonebook(contact_name, phone_number) VALUES(%s, %s) ON CONFLICT DO NOTHING"
    params = load_config()
    
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # Открываем CSV файл для чтения
                with open(file_path, mode='r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        # row[0] - это имя, row[1] - это телефон
                        cur.execute(sql, (row[0], row[1]))
                
                conn.commit()
                print(f"Данные из файла {file_path} успешно загружены!")
                
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка при загрузке CSV: {error}")

# ЕДИНЫЙ ТОЧКА ЗАПУСКА
if __name__ == '__main__':
    # 1. Проверяем/создаем таблицу
    create_table()
    
    # 2. Ручной ввод
    user_name = input("Введите имя: ")
    user_phone = input("Введите телефон: ")
    insert_contact(user_name, user_phone)
    
    # 3. Загрузка из файла
    insert_from_csv('contacts.csv')

def update_contact(name, new_phone):
    """ Обновление номера телефона по имени контакта """
    sql = "UPDATE phonebook SET phone_number = %s WHERE contact_name = %s"
    try:
        params = load_config()
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_phone, name))
                updated_rows = cur.rowcount # Считаем, сколько строк изменилось
                conn.commit()
                if updated_rows > 0:
                    print(f"Контакт '{name}' обновлен. Новый номер: {new_phone}")
                else:
                    print(f"Контакт с именем '{name}' не найден.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка при обновлении: {error}")

def delete_contact(name):
    """ Удаление контакта по имени """
    sql = "DELETE FROM phonebook WHERE contact_name = %s"
    try:
        params = load_config()
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name,))
                deleted_rows = cur.rowcount
                conn.commit()
                if deleted_rows > 0:
                    print(f"Контакт '{name}' успешно удален.")
                else:
                    print(f"Контакт '{name}' не найден.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка при удалении: {error}")

if __name__ == '__main__':
    # ... твой предыдущий код (создание, вставка) ...
    
    # Давай проверим обновление
    update_contact('Ivan', '87009998877')
    
    # И удалим кого-нибудь для теста
    delete_contact('Тимурбэк')