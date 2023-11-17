#!/usr/bin/python3
"""
    lists all states with a name starting with N
    from the database hbtn_0e_0_usa
    Usage: ./1-filter_states.py <username> <password> <database>
"""

import MySQLdb as sql
import sys


def fetch_states_with_initial_n(username, password, database):
    try:
        with sql.connect(user=username, passwd=password, db=database) as db:
            with db.cursor() as cursor:
                cursor.execute("SELECT * FROM `states` ORDER BY `id`")
                states = [
                    state for state in cursor.fetchall()
                    if state[1][0] == 'N'
                ]
                return states
    except sql.Error as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("⚠️  Usage: python3 script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    result = fetch_states_with_initial_n(username, password, database)

    for state in result:
        print(state)
