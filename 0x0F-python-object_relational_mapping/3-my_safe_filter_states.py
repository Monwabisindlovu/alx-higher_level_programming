#!/usr/bin/python3
"""
Script that takes in an argument and displays
all values in the states table of
hbtn_0e_0_usa where name matches the argument (safe from MySQL injection).
"""
import MySQLdb
import sys

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cur = db.cursor()
        
        state_name = sys.argv[4]
        
        # Using parameters to prevent SQL injection
        query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
        cur.execute(query, (state_name,))
        
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: %s" % str(e))

