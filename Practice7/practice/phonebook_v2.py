import psycopg2
from config import get_connection

class PhoneBookApp:
    def __init__(self):
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def search(self, text):
        self.cur.execute("SELECT * FROM get_contacts_pattern(%s)", (text,))
        return self.cur.fetchall()
    
    def upsert(self, name, phone):
        self.cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
        self.conn.commit()

    def bulk_insert(self, names, phones):
        self.cur.execute("CALL bulk_insert_contacts(%s, %s)", (names, phones))
        self.conn.commit()

    def get_page(self, limit, offset):
        self.cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
        return self.cur.fetchall()
    
    def delete(self, identifier):
        self.cur.execute("CALL delete_contact_flexible(%s)", (identifier,))
        self.conn.commit()

    def __del__(self):
        if hasattr(self, 'cur'): self.cur.close()
        if hasattr(self, 'conn'): self.conn.close()

if __name__ == "__main__":
    app = PhoneBookApp()
    
    app.upsert('Almat', '87071112233')
    app.bulk_insert(['Damir', 'TestUser'], ['87015554433', '87029990011'])
    
    print("Результат поиска:", app.search('Alm'))
    print("Первая страница (2 контакта):", app.get_page(2, 0))