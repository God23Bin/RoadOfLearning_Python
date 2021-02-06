import sqlite3 as sql3
conn = sql3.connect('test.db')

cur = conn.cursor()

# sql_table_genre = '''CREATE TABLE genre(
#             g_id integer PRIMARY KEY ,
#             g_name varchar(10) NOT NULL
#         )'''
#
# sql_table_book = '''CREATE TABLE book(
#             b_id integer PRIMARY KEY ,
#             b_name varchar(10) NOT NULL ,
#             b_price float NOT NULL ,
#             b_date text NULL ,
#             b_genre REFERENCES genre(g_id) ON UPDATE CASCADE ON DELETE CASCADE
#         )'''
#
# cur.execute(sql_table_genre)
# cur.execute(sql_table_book)

# cur.execute('''CREATE TABLE genre(
#             g_id integer PRIMARY KEY ,
#             g_name varchar(10) NOT NULL
#         )''')
#
# cur.execute('''CREATE TABLE book(
#             b_id integer PRIMARY KEY ,
#             b_name varchar(10) NOT NULL ,
#             b_price float NOT NULL ,
#             b_date text NULL ,
#             b_genre REFERENCES genre(g_id) ON UPDATE CASCADE ON DELETE CASCADE
#         )''')
cur.execute('''ALTER TABLE genre ADD COLUMN g_comm text NULL ''')

insert_sql = '''insert into genre values(1, 'History', 'to know the history of human world')'''
insert_sql2 = '''insert into genre values(2, 'Social Science', 'to know Science')'''
insert_sql3 = "insert into genre values(?,?,?)"

cur.execute(insert_sql)
cur.execute(insert_sql2)
cur.execute(insert_sql3,(3, 'Java', 'to be better Java Developer'))