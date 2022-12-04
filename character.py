"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""

from prettytable import PrettyTable


class Character:

    def __init__(self, name):
        self.__name = name
        self.__current_hp = 5
        self.__max_hp = 5
        self.__current_mana = 5
        self.__max_mana = 5
        self.__level = 1
        self.__experience = 0
        self.__current_location = [0, 0]

    def set_current_hp(self, difference):
        self.__current_hp += difference

    def set_max_hp(self, level_up_hp):
        self.__max_hp += level_up_hp

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

    def get_max_hp(self):
        return self.__max_hp

    def get_current_mana(self):
        return self.__current_mana

    def change_current_mana(self, change):
        self.__current_mana += change

    def get_max_mana(self):
        return self.__max_mana

    def get_level(self):
        return self.__level

    def get_experience(self):
        return self.__experience

    def get_current_location(self):
        return self.__current_location

    def print_stat(self):
        headers = ["Character", "Level", "HP", "Experience", "Current location"]
        info = [self.__name, self.__level, self.__current_hp, self.__experience, self.__current_location]
        table = PrettyTable(headers)
        table.add_row(info)
        print(table)

    def move_to(self, direction):
        if direction == 'North':
            self.__current_location[0] -= 1
        elif direction == 'South':
            self.__current_location[0] += 1
        elif direction == 'West':
            self.__current_location[1] -= 1
        elif direction == 'East':
            self.__current_location[1] += 1


def main():
    pass


if __name__ == '__main__':
    main()
