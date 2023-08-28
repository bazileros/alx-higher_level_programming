#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    re_turn = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            re_turn += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (re_turn)