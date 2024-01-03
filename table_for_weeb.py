
import sqlite3 as sq
cons=sq.connect('store.db')
cur_=cons.cursor()
z=cur_.execute#nam,eid,pass,gender,country,refeid
z('select * from RATINGS;')
w=cur_.fetchall()
for i in w:
    print('w',i)
z('select * from storage;')
a=cur_.fetchall()
for j in a:
    print(a)
cons.commit()
