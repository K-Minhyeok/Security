import sqlite3
from binascii import hexlify,unhexlify

c = sqlite3.connect('test.db')
cursor = c.cursor()

name = input('name? ').encode()
age = input('age? ').encode()
input_name = hexlify(name).decode()
input_age = hexlify(age).decode()

print(f'sql을 통해 db에 저장되는 이름 데이터 :  {input_name}')
print(f'sql을 통해 db에 저장되는 이름 데이터 : {input_age}')

cursor.execute(f"INSERT INTO test VALUES('{input_name}','{input_age}')")
cursor.execute('SELECT * FROM test')
out = cursor.fetchall()

print(unhexlify(out[0][0]).decode())
print(unhexlify(out[0][1]).decode())

