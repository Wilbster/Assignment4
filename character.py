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
        self.__level = 1
        self.__current_hp = 5
        self.__max_hp = 5
        self.__current_mana = 5
        self.__max_mana = 5
        self.__experience = 0
        self.__current_location = [0, 0]

    def change_current_hp(self, difference):
        self.__current_hp += difference

    def set_current_hp(self, value):
        self.__current_hp = value

    def set_max_hp(self, level_up_hp):
        self.__max_hp = level_up_hp

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

    def set_current_mana(self, value):
        self.__current_mana = value

    def change_current_mana(self, change):
        self.__current_mana += change

    def get_max_mana(self):
        return self.__max_mana

    def set_max_mana(self, value):
        self.__max_mana = value

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


def character_should_level(character: Character) -> bool:
    """
    Check whether the Character should level up.

    :param character: an object of type Character
    :return: a boolean
    """
    if character.get_level() < 2 and character.get_experience() > 29:
        return True
    elif character.get_level() < 3 and character.get_experience() > 149:
        return True
    else:
        return False


def level_up(character: Character) -> None:
    """
    Level up a character in Witcher: Fang of the Devil.

    :param character: an object of the Character class
    :precondition: character must have enough experience but not yet have been levelled up
    postcondition: character is levelled up
    """
    if character.get_level() < 2 and character.get_experience() > 29:
        character.set_level()
    elif character.get_level() < 3 and character.get_experience() > 149:
        character.set_level()
    print(f"Congratulations! You have levelled up! You now now a level {character.get_level()} Witcher!")
    character.set_max_hp(character.get_max_hp()*character.get_level()**2)
    character.set_max_mana(character.get_max_mana()*character.get_level()**2)
    character.set_current_hp(character.get_max_hp())
    character.set_current_mana(character.get_max_mana())
    print(f"Your health has been restored to its new maximum of {character.get_current_hp()}")
    print(f"Your mana has been restored to its new maximum of {character.get_current_mana()}")


def main():
    """
     Drive the program.
     """


if __name__ == '__main__':
    main()
