#!/usr/bin/python3
def element_at(my_list, idx):
    lenght = len(my_list)
    if idx < 0:
        print("None")
    elif idx > lenght:
        print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
