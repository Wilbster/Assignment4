"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""

from prettytable import PrettyTable


class Enemy:
    """
    A simple enemy has a name, description, hp and experience.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize an Enemy object.

        :param name: a non-empty string
        :precondition: name must be a non-empty string
        :postcondition: initializes parameters of Enemy object. Name is initialized with given value,
        description is initialized as empty strings, hp and experience are initialized with zero

        >>> little_monster = Enemy("Tom")
        >>> type(little_monster)
        <class 'enemy.Enemy'>
        >>> little_monster
        Enemy(Tom, 0, 0, )
        """
        self.__enemy_name = name
        self.__description = ""
        self.__hp = 0
        self.__experience = 0

    def get_name(self) -> str:
        """
        Get name of this Enemy object.

        :postcondition: returns enemy's name as a string
        :return: a string

        >>> little_monster = Enemy("Tom")
        >>> little_monster.get_name()
        'Tom'
        """
        return self.__enemy_name

    def set_description(self, description: str) -> None:
        """
        Set description for this Enemy object.

        :param description: a non-empty string
        :precondition: description must be a non-empty string
        :postcondition: sets given description value to a description attribute

        >>> little_monster = Enemy("Tom")
        >>> little_monster.set_description("Fluffy")
        >>> little_monster
        Enemy(Tom, 0, 0, Fluffy)
        """
        self.__description = description

    def set_hp(self, hp: int) -> None:
        """
        Set hp for this Enemy object.

        :param hp: a positive int
        :precondition: hp must be a positive int
        :postcondition: sets given hp value to a hp attribute

        >>> little_monster = Enemy("Tom")
        >>> little_monster.set_hp(5)
        >>> little_monster
        Enemy(Tom, 5, 0, )
        """
        self.__hp = hp

    def get_hp(self) -> int:
        """
        Get hp for this Enemy object

        :postcondition: gets hp of Enemy object that invoked method
        :return: an int

        >>> little_monster = Enemy("Tom")
        >>> little_monster.get_hp()
        0
        >>> little_monster.set_hp(5)
        >>> little_monster.get_hp()
        5
        """
        return self.__hp

    def set_experience(self, experience):
        """
        Set experience for Enemy object.

        :param experience: a positive int
        :precondition: experience must be a positive int
        :postcondition: sets given experience value to a experience attribute

        >>> little_monster = Enemy("Tom")
        >>> little_monster.set_experience(5)
        >>> little_monster
        Enemy(Tom, 0, 5, )
        """
        self.__experience = experience

    def get_experience(self) -> int:
        """
        Get experience of this Enemy object.

        :postcondition: returns this Enemy object experience value
        :return: an int

        >>> little_monster = Enemy("Tom")
        >>> little_monster.set_experience(7)
        >>> little_monster.get_experience()
        7
        """
        return self.__experience

    def change_hp(self, damage: int) -> None:
        """
        Calculate this Enemy object hp.

        :param damage: an int
        :precondition: damage must be an int
        :postcondition: calculates and updates this object hp by adding given damage value

        >>> little_monster = Enemy("Tom")
        >>> little_monster.set_hp(5)
        >>> little_monster.change_hp(-2)
        >>> little_monster.get_hp()
        3
        """
        self.__hp += damage

    def show_enemy_stat(self) -> None:
        """
        Print out this object name, hp and experience in table.

        :postcondition: produces side effect and prints out this Enemy object name, hp and description in a table
        """
        headers = ["Enemy", "HP", "Experience"]
        info = [self.__name, self.__hp, self.__experience]
        table = PrettyTable(headers)
        table.add_row(info)
        print(table)

    def describe_enemy(self) -> None:
        """
        Display description.

        :postcondition: produces side effect and prints out description of this Enemy object as a string

        >>> little_monster = Enemy("Tom")
        >>> little_monster.set_description("Fluffy")
        >>> little_monster.describe_enemy()
        Fluffy
        """
        print(self.__description)

    def __str__(self) -> str:
        """
        Build a string representation of this Enemy object.

        :postcondition: builds a string representation of this Enemy object in the following format
        {self.__enemy_name} | HP: {self.__hp}, Experience: {self.__experience}, ' \
               f'description: {self.__description}
        :return: a string

        >>> little_monster = Enemy("Tom")
        >>> little_monster.set_description("Fluffy")
        >>> little_monster.set_hp(10)
        >>> little_monster.set_experience(5)
        >>> print(little_monster)
        Tom | HP: 10, Experience: 5, description: Fluffy
        """
        return f'{self.__enemy_name} | HP: {self.__hp}, Experience: {self.__experience}, ' \
               f'description: {self.__description}'

    def __repr__(self) -> str:
        """
        Build a string representation of this Enemy object type and state.

        :postcondition: builds a string representation of the location object in the following format
        {self.__class__.__name__}({self.__enemy_name}, {self.__hp}, {self.__experience}, {self.__description})
        :return: a string

        >>> little_monster = Enemy("Tom")
        >>> little_monster.set_description("Fluffy")
        >>> little_monster.set_hp(10)
        >>> little_monster.set_experience(5)
        >>> little_monster
        Enemy(Tom, 10, 5, Fluffy)
        """
        return f'{self.__class__.__name__}({self.__enemy_name}, {self.__hp}, {self.__experience}, {self.__description})'
