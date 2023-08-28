#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0

    for i in range(min(x, len(my_list))):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break

    print()
    return count
