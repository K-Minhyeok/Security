import sqlite3

c = sqlite3.connect('test.db')
cursor = c.cursor()

name = input('name? ')
age = input('age? ')
data = name,age

cursor.execute('CREATE TABLE test(name text,age integer)')


cursor.execute(f"INSERT INTO test VALUES(?,?)",data)
cursor.execute('SELECT * FROM test')
out = cursor.fetchall()
print(out)
c.commit()

