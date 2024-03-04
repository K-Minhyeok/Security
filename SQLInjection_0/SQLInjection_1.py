import sqlite3
c=sqlite3.connect('test.db')
cursor =c.cursor()

user_name = input('이름을 입력하세요')
user_age = input('나이')
user_age = int(user_age)

cursor.execute(f"INSERT INTO test  VALUES ('{user_name}',{user_age})")

cursor.execute("SELECT * FROM test")
out = cursor.fetchall()
print(out)
c.commit()

