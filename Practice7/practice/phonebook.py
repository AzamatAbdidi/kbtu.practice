import psycopg2
import csv
from config import get_connection


def creating_table():
    conn = get_connection()
    cur = conn.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS telefony (
        contact_id SERIAL PRIMARY KEY,
        name VARCHAR(200) NOT NULL,
        phone VARCHAR(100) UNIQUE NOT NULL
    );
       """
    try:
     cur.execute(sql)
     conn.commit()
     print("Table 'telefony' was created succesfully")
    except Exception as err:
       print(f"Error with creating table {err}")
    finally:
       cur.close()
       conn.close()
    
if __name__ == "__main__":
   creating_table()

def add_contact(user_name, user_phone):
   conn = get_connection()
   cur = conn.cursor()

   sql = "INSERT INTO telefony (name,phone) VALUES (%s,%s)"

   try:
      cur.execute(sql, (user_name, user_phone))
      conn.commit()
      print(f"The contact {user_name} was succesfully added!")
   except Exception as err:
      print(f"The are error with adding contact {err}")
      conn.rollback()
   finally:
      cur.close()
      conn.close()

if __name__ == "__main__":
   creating_table()
   print("--- Adding new contact ---")
   name_input = input("Type the user name: ")
   phone_input = input("Type the phone number: ")

   add_contact(name_input, phone_input)
      
def import_csv(filename):
   conn = get_connection()
   cur = conn.cursor()

   try:
      with open(filename, mode='r', encoding='utf-8') as f:
         reader = csv.DictReader(f)

         for row in reader:
            cur.execute(
               "INSERT INTO telefony (name, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING",
               (row['name'], row['phone'])
            )
      conn.commit()
      print(f"Data from file '{filename}' was succesfully imported")
   except Exception as e:
      print(f"Error with importing from CSV: {e}")
      conn.rollback()
   finally:
      cur.close()
      conn.close()

if __name__ == "__main__":
   import_csv('contacts.csv')

def update_contact(targate_name, new_phone):
   conn = get_connection()
   cur = conn.cursor()

   sql = "UPDATE telefony SET phone = %s WHERE name = %s"
   cur.execute(sql, (new_phone, targate_name))
   conn.commit()
   print(f"The contact {targate_name} was updated")
   cur.close()
   conn.close()

if __name__ == "__main__":
    update_contact('Aidyn', '87010009988') 

def delete_contact(target_name):
    conn = get_connection()
    cur = conn.cursor()
    
    sql = "DELETE FROM telefony WHERE name = %s"
    
    cur.execute(sql, (target_name,)) # Запятая нужна, чтобы Python понял, что это кортеж
    conn.commit()
    
    print(f"Контакт {target_name} удален.")
    cur.close()
    conn.close()
   
def query_contacts(search_name):
    conn = get_connection()
    cur = conn.cursor()
    
    
    sql = "SELECT * FROM telefony WHERE name ILIKE %s"
    
    cur.execute(sql, (f"%{search_name}%",))
    rows = cur.fetchall()
    if not rows:
        print("Ничего не найдено.")
    else:
        print("\n--- Результаты поиска ---")
        for row in rows:
            print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")
    
    cur.close()
    conn.close()