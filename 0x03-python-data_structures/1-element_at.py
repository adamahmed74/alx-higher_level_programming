#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        print("None")
    elif idx > my_list:
        print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
