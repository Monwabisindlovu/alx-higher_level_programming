#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cur = db.cursor()
        
        # Using a JOIN to get city names along with their respective state names
        query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
        cur.execute(query)

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

