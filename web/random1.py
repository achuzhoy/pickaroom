#!/usr/bin/env python
#for this script to works- you need:
# a db on the localhost
# a table named vacation with 2 columns:roomname,family (strings), while roomname is the primary key
# 3 arguments (username,password, dbname)

import random
import MySQLdb
import sys

def print_results(cursor,errorcheck):
    sql = "select * from vacation;"
    cursor.execute(sql)
    sqloutput = cursor.fetchall()
    if (len(sqloutput)) == 0:
        return("No results yet")
    output=errorcheck
    for row in sqloutput:
        output="%s%s family has randomly selected room %s\n" % (output, row[0], row[1])
    return output

def populate_db(cursor,familyname,rooms):
    if len(rooms) > 0:
        room=(rooms[(random.choice(range(len(rooms))))])
        sql = "INSERT INTO vacation(family,roomname)  VALUES ('%s', '%s' );" %   (familyname,room)
        try:
            cursor.execute(sql)
        except:
            return  "################################# Sorry, this family name was already used. ############################\n"
        rooms.remove(room)
    else:
        return "##################################  Sorry, no more available rooms #####################################\n"


def eliminate_occupied_rooms(cursor,rooms):
    sql = "select * from vacation;"
    cursor.execute(sql)
    sqloutput = cursor.fetchall()
    for line  in sqloutput:
        try:
            rooms.remove(line[1])
        except:
            pass
    if len(rooms) == 0:
        print("Sorry. No more available rooms. Exiting...")
    return rooms


def main(familyname):
    db_user="<string>"
    db_passwd="<string>"
    db_name="<string>"
    
    db = MySQLdb.connect(host="localhost", user=db_user, passwd=db_passwd,db=db_name)   
    cursor = db.cursor()
    all_rooms=["one","two","three","four","five","six","seven","eight"]
    rooms=eliminate_occupied_rooms(cursor,all_rooms)
    errorcheck=populate_db(cursor,familyname,rooms)
    if not errorcheck:
        errorcheck="\n"
    db.commit()
    output=print_results(cursor,errorcheck)
    db.close()
    return output

if __name__ == '__main__':
    main()
