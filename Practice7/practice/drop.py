import psycopg2
from config import load_config

def drop_table():
    conn = None
    try:
        params = load_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        # Команда DROP TABLE удаляет таблицу полностью
        cur.execute("DROP TABLE IF EXISTS phonebook CASCADE;")
        
        conn.commit()
        cur.close()
        print("Таблица 'phonebook' успешно удалена!")
    except Exception as error:
        print(f"Не удалось удалить: {error}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    drop_table()