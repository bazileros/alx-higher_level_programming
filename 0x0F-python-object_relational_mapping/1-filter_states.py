#!/usr/bin/python3
"""
    lists all states with a name starting with N
    from the database hbtn_0e_0_usa
    Usage: ./1-filter_states.py <username> <password> <database>
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
                    "SELECT * FROM `states` WHERE name LIKE BINARY 'N%'"
                )
                [print(state) for state in cursor.fetchall()]

    except sql.Error as e:
        print(f"❌ Error: {e}")
