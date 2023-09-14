#!/usr/bin/python3

"""Script that takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = %s\
              ORDER BY states.id ASC", (sys.argv[4],))

    all_data = c.fetchall()

    for data in all_data:
        print(data)

    c.close()
    db.close()
