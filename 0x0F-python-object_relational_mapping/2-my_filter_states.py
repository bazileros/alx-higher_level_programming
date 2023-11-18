#!/usr/bin/python3
"""
"""

import sys
import MySQLdb as sql

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        with sql.connect(user=username, passwd=password, db=database) as db:
            with db.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM `states` WHERE name = %s ORDER BY id ASC",
                    (state_name,),
                )
                states = cursor.fetchall()
                for state in states:
                    print(state)
    except sql.Error as e:
        print(f"❌ Error: {e}")
