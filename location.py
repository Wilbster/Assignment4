"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""


class Location:

    def __init__(self, location_type):
        self.__location_type = location_type
        self.__description = ""
        self.__enemy = ""

    def get_location_type(self):
        return self.__location_type

    def set_description(self, description):
        self.__description =  description

    def get_description(self):
        return self.__description

    def set_enemy(self, enemy):
        self.__enemy = enemy

    def get_enemy(self):
        return self.__enemy

    def describe_location(self):
        print(self.__description)

    def __str__(self):
        return f'{self.__location_type}, {self.__description}, {self.__enemy}'

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.__location_type}", {self.__description}, {self.__enemy})'
