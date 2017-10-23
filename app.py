#!/usr/bin/env python
import MySQLdb

def main():
   db = MySQLdb.connect(host="10.130.34.252",user="root",passwd="redhat",db="vacation")
   cursor = db.cursor()
   cursor.execute("insert into rooms (familyname,roomname) values ('a1','b1');)
   db.commit()
   db.close()


if __name__ == '__main__':
    main()
