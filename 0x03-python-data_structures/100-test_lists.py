import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
lits = ['hello', 'World']
lib.print_python_list_info(lits)
del lits[1]
lib.print_python_list_info(lits)
lits = lits + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(lits)
lits = []
lib.print_python_list_info(lits)
lits.append(0)
lib.print_python_list_info(l)
lits.append(1)
lits.append(2)
lits.append(3)
lits.append(4)
lib.print_python_list_info(lits)
lits.pop()
lib.print_python_list_info(lits)
