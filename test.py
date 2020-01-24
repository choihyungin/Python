import pymysql

conn = pymysql.connect(
    host = 'localhost', user='root', password='1234',
    db = 'python', charset='utf8'
)

cursor = conn.cursor()

sql = '''CREATE TABLE mysql (
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            title VARCHAR(100), content VARCHAR(100))'''
cursor.execute(sql)

conn.commit()

cursor.close()
conn.close()