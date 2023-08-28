#!/usr/bin/python3
"""
This is a test script for the 101-safe_function.py module.
"""

import lib


def main():
    """
    Main function for testing the lib.print_python_list function.
    """
    l = []
    lib.print_python_list(l)

    l.append(0)
    lib.print_python_list(l)

    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    lib.print_python_list(l)

    l.pop()
    lib.print_python_list(l)

    l = ["School"]
    lib.print_python_list(l)
    lib.print_python_bytes(l)

    f = 3.14
    lib.print_python_float(f)

    l = [-1.0, -0.1, 0.0, 1.0, 3.14, 3.14159,
         3.14159265, 3.141592653589793238462643383279502884197169399375105820974944592307816406286]
    print(l)
    lib.print_python_list(l)
    lib.print_python_float(l)


if __name__ == "__main__":
    main()
