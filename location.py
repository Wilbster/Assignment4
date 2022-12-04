"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""

import textwrap

from enemy import Enemy


class Location:
    """
    A simple location has a type, description and enemy.
    """

    def __init__(self, location_type: str):
        """
        Initialize a Location object.

        :param location_type: a non-empty string
        :precondition: location_type must be a non-empty string
        :postcondition: initializes parameters of Location object. Location-type is initialized with given value,
        description and enemy are initialized as empty strings
        """
        self.__location_type = location_type
        self.__description = ""
        self.__enemy = ""

    def get_location_type(self) -> str:
        """
        Get location type.

        :postcondition: returns location type as a string
        :return: a string
        """
        return self.__location_type

    def set_description(self, description: str):
        """
        Set description.

        :param description: a string
        :precondition: description must be a string
        :postcondition: sets value of description attribute as string
        """
        self.__description = description

    def get_description(self) -> str:
        """
        Get description.

        :postcondition: returns value of description as a string
        :return: a string
        """
        return self.__description

    def set_enemy(self, enemy: Enemy):
        """
        Set description.

        :param enemy: an Enemy
        :precondition: enemy must be an object of type Enemy
        :postcondition: sets Enemy object to enemy attribute
        """
        self.__enemy = enemy

    def get_enemy(self):
        """
        Get enemy.

        :postcondition: returns object of type Enemy
        :return: an Enemy
        """
        return self.__enemy

    def describe_location(self) -> None:
        """
        Display description.

        :postcondition: produces side effect and prints out description as a string
        """
        description = textwrap.fill(self.__description, width=100)
        print(description)

    def __str__(self) -> str:
        """
        Build a string representation of the location object.

        :postcondition: builds a string representation of the location object in the following format
        {self.__location_type}, {self.__description}, {self.__enemy}
        :return: a string
        """
        return f'{self.__location_type}, {self.__description}, {self.__enemy}'

    def __repr__(self) -> str:
        """
        Build a string representation of the location object type and state.

        :postcondition: builds a string representation of the location object in the following format
        {self.__class__.__name__}("{self.__location_type}", {self.__description}, {self.__enemy})
        :return: a string
        """
        return f'{self.__class__.__name__}("{self.__location_type}", {self.__description}, {self.__enemy})'
