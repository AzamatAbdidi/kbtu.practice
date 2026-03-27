import psycopg2
from configparser import ConfigParser

def load_config(filename="database.ini" , section = "postgresql"):
    # Читает файл .ini и возвращает словарь с параметрами подключения
    pars = ConfigParser()
    pars.read(filename)
    
    conf = {}
    if pars.has_section(section):
        params = pars.items(section)
        for parametr in params:
            conf[parametr[0]]=parametr[1]
    else:
        # Если забыл создать файл или секцию, Python об этом скажет
        # это сейфти зона 
        raise Exception(f'Секция {section} не найдена в файле {filename}')
    
    return conf 


def connect():
    # Надо установить соедениение с сервером постгре
 connection = None
 try:
    #  Загружаем то что уже настраивали в той функций 
    params = load_config()
    # 2. Подключаемся к серверу (распаковываем словарь через **)
    print('Подключаюсь к базе данных...')
    connection = psycopg2.connect(**params)

    # 3. Создаем курсор для выполнения команд
    cur = connection.cursor()
        
    # Выполняем тестовый запрос, чтобы узнать версию базы
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)
        
        # Закрываем курсор
    cur.close()
    print('Соединение установлено успешно!')

 except (Exception, psycopg2.DatabaseError) as error:
        # Если пароль неверный или база не создана, ошибка выведется здесь
     print(f"Ошибка при подключении: {error}")
 finally:
        # В конце обязательно закрываем соединение, если оно было открыто
  if connection is not None:
            connection.close()
            print('Связь с базой закрыта.')

if __name__ == '__main__':
    connect()