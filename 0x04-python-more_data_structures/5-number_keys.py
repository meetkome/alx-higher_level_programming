#!/usr/bin/python3

def number_keys(a_dictionary):
    numkeys = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        numkeys += 1

    return (numkeys)
