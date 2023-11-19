#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa
    Usage: ./4-cities_by_state.py <username> <password> <database>
"""

import MySQLdb as sql
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        with sql.connect(user=username, passwd=password, db=database) as db:
            with db.cursor() as cursor:
                cursor.execute(
                    "SELECT `cities`.`id`, `cities`.`name`, `states`.`name`\
                    FROM cities\
                    INNER JOIN states\
                    ON cities.state_id = states.id\
                    ORDER BY cities.id ASC"
                )
                [print(city) for city in cursor.fetchall()]

    except sql.Error as e:
        print(f"❌ Error: {e}")
