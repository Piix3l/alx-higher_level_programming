#!/usr/bin/python3
""" Class inherting """


class MyList(list):
    """ inherit from list. """

    def print_sorted(self):
        print(sorted(self))
