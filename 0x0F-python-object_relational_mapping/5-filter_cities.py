#!/usr/bin/python3
""" takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb as sql
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        with sql.connect(user=username, passwd=password, db=database) as db:
            with db.cursor() as cursor:
                cursor.execute(
                    "SELECT cities.id, cities.name\
                    FROM cities\
                    INNER JOIN states\
                    ON cities.state_id = states.id\
                    WHERE states.name = %s\
                    ORDER BY cities.id ASC",
                    (state_name,),
                )
                [print(city) for city in cursor.fetchall()]

    except sql.Error as e:
        print(f"❌ Error: {e}")
