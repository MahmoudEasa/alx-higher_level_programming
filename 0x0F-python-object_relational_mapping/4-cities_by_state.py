#!/usr/bin/python3

"""Script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
              LEFT JOIN states ON cities.state_id = states.id\
              ORDER BY cities.id ASC")

    all_data = c.fetchall()

    for data in all_data:
        print(data)

    c.close()
    db.close()
