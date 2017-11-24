#!/usr/bin/env python
#for this script to works- you need:
# a db on the localhost
# a table named vacation with 2 columns:roomname,family (strings), while roomname is the primary key
# 3 arguments (username,password, dbname)

import random
import MySQLdb
import sys

def print_results(cursor):
    sql = "select * from vacation;"
    cursor.execute(sql)
    sqloutput = cursor.fetchall()
    if (len(sqloutput)) == 0:
        print("No results yet")
    for row in sqloutput:
        print("%s family has randomly selected room %s" % (row[0], row[1]))

def populate_db(cursor,familyname,rooms):
    room=(rooms[(random.choice(range(len(rooms))))])
    #while (len(rooms) > 0 ):
    sql = "INSERT INTO vacation(family,roomname)  VALUES ('%s', '%s' );" %   (familyname,room)
    try:
        cursor.execute(sql)
    except:
        print "Error: Duplication - this family name was already used.\nClean the database if you want to insert it again."
        sys.exit(1)
    rooms.remove(room)

def get_name_input():
    name=raw_input("When you're ready to autoselect the room, enter your family name?\n")
    if len(name) == 0:
        print("You're supposed to enter your family name. Exiting...")
        sys.exit(1)
    elif not name.isalpha():
        print("You're supposed to enter your family name. Exiting...")
        sys.exit(1)
    print("Your family name is: %s" % name)
    return name

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
        sys.exit(0)
    return rooms

def get_selection():
    print("What would you like to do?")
    print("1. See the lottery results")
    print("2. Try your luck")
    response=raw_input()
    try:
        if int(response) != 1 and int(response)!= 2:
            print "Error. Wrong selection. Can be 1 or 2. Exiting..."
            sys.exit(1)
    except(ValueError):
        print("Integers 1 or 2 only please. Exiting...")
        sys.exit(1)
    return(int(response))

def check_args():
    if len(sys.argv) < 4:
        print("Error. Must provide username,password,dbname as arguments to the script")
        sys.exit(1)
    else:
        db_user=sys.argv[1]
        db_passwd=sys.argv[2]
        db_name=sys.argv[3]
        return(db_user,db_passwd,db_name)

def main():
    (db_user,db_passwd,db_name)=check_args()
    
    response=get_selection()
    db = MySQLdb.connect(host="localhost", user=db_user, passwd=db_passwd,db=db_name)   
    cursor = db.cursor()
    if response == 2:
        familyname=get_name_input()
        all_rooms=["one","two","three","four","five","six","seven","eight"]
        rooms=eliminate_occupied_rooms(cursor,all_rooms)
        populate_db(cursor,familyname,rooms)
        db.commit()
    print_results(cursor)
    db.close()

if __name__ == '__main__':
    main()
