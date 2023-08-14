#!/usr/bin/python3
# 0-print_list_integer.py

def print_list_integers(my_list=[]):
    '''Print all intergers of the list'''
    for contents in range(len(my_list)):
        print("{:d}".format(my_list[contents]))
