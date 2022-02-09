'''import asyncio
import orm
from models import User


async def test():
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='winger123456@', db='awesome')
    a = User(name='Administrator', email='admin@example.com', passwdord='1234567890', image='about:blank')
    x = User(name='xian_wen', email='xian_wen@example.com', password='1234567890', image='about:blank')
    t = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')
    await a.save()
    await x.save()
    await t.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test())'''


import mysql.connector

# change root password to yours:
'''conn = mysql.connector.connect(user='root', password='winger123456@')
cursor = conn.cursor()
# 创建awesome数据库：
cursor.execute('create database awesome')
print('Create database successfully.')
cursor.close()
conn.close()'''

conn = mysql.connector.connect(user='root', password='winger123456@', database='awesome')
cursor = conn.cursor()
# 删除users表：
cursor.execute('drop table if exists users')

# 创建users表:
sql = """create table users (
         id varchar(50) NOT NULL,
         name varchar(20),
         email varchar(20),
         password varchar(100),
         image varchar(5000),
         admin varchar(20),
         created_at float(20)
         )"""

cursor.execute(sql)

# 删除blogs表：
cursor.execute('drop table if exists blogs')

# 创建blogs表:
sql = """create table blogs (
         id varchar(50) NOT NULL,
         user_id varchar(50),
         user_name varchar(50),
         user_image varchar(5000),
         name varchar(50),
         summary varchar(200),
         content text,
         created_at float(20)
         )"""

cursor.execute(sql)

# 删除comments表：
cursor.execute('drop table if exists comments')

# 创建blogs表:
sql = """create table comments (
         id varchar(50) NOT NULL,
         blog_id varchar(50),
         user_id varchar(50),
         user_name varchar(50),
         user_image varchar(5000),
         content text,
         created_at float(20)
         )"""

cursor.execute(sql)

#cursor.execute('create table users (name varchar(20) primary key, email varchar(20), password varchar(20), image varchar(20)')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into users (id, name, email, password, image, created_at) values (%s, %s, %s, %s, %s, %s)', ('1', 'Hannah', 'example@example.com', '123456', 'about:blank', 1634567))
cursor.execute('insert into users (id, name, email, password, image, created_at) values (%s, %s, %s, %s, %s, %s)', ('2', 'Wenger', 'admin@example.com', '123456', 'about:blank', 1634568))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from users where name = %s', ('Wenger',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()