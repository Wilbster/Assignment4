"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""

from tabulate import tabulate


class Character:

    hp = 5

    def __init__(self, name):
        self.__name = name
        self.__current_hp = Character.hp
        self.__level = 1
        self.__experience = 0
        self.__current_location = (0, 0)

    def set_current_hp(self, difference):
        self.__current_hp += difference

    def set_level(self):
        self.__level += 1

    def set_experience(self, gained_experience):
        self.__experience += gained_experience

    def set_current_location(self, new_coordinates):
        self.__current_location = new_coordinates

    def get_name(self):
        return self.__name

    def get_current_hp(self):
        return self.__current_hp

    def get_level(self):
        return self.__level

    def get_experience(self):
        return self.__experience

    def get_current_location(self):
        return self.__experience

    def print_stat(self):
        headers = ["Character", "Level", "HP", "Experience", "Current location"]
        info = [self.__name, self.__level, self.__current_hp, self.__experience, self.__current_location]
        print(tabulate(info, headers))


def main():
    pass


if __name__ == '__main__':
    main()
