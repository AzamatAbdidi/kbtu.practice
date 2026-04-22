import psycopg2
def get_connection():
    conn = psycopg2.connect(
     host = "localhost",
     user="postgres",
     password="scam1717",
     database="telefony"
)
    return conn


if __name__ == "__main__":
    test_cnn = get_connection()
    if test_cnn:
        print("Connection between base 'telefony' is horosho")
        test_cnn.close()
