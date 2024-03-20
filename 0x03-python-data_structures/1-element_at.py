#!/usr/bin/python3
def element_at(my_list, idx):
    variable = len(my_list)
    if idx < 0 or idx >= variable:
        print("None")
    else:
        return my_list[idx]
