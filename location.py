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

        >>> test_location = Location("Hall")
        >>> type(test_location)
        <class 'location.Location'>
        >>> test_location
        Location("Hall", , )
        """
        self.__location_type = location_type
        self.__description = ""
        self.__enemy = ""

    def get_location_type(self) -> str:
        """
        Get location type.

        :postcondition: returns location type as a string
        :return: a string

        >>> test_location = Location("Hall")
        >>> test_location.get_location_type()
        'Hall'
        """
        return self.__location_type

    def set_description(self, description: str) -> None:
        """
        Set description.

        :param description: a string
        :precondition: description must be a string
        :postcondition: sets value of description attribute as string

        >>> test_location = Location("Hall")
        >>> test_location.set_description("test description")
        >>> test_location
        Location("Hall", test description, )
        """
        self.__description = description

    def get_description(self) -> str:
        """
        Get description.

        :postcondition: returns value of description as a string
        :return: a string

        >>> test_location = Location("Hall")
        >>> test_location.set_description("test description")
        >>> test_location.get_description()
        'test description'
        """
        return self.__description

    def set_enemy(self, enemy: Enemy) -> None:
        """
        Set description.

        :param enemy: an Enemy
        :precondition: enemy must be an object of type Enemy
        :postcondition: sets Enemy object to enemy attribute

        >>> test_location = Location("Hall")
        >>> test_location.set_enemy(Enemy("Monster"))
        >>> type(test_location.get_enemy())
        <class 'enemy.Enemy'>
        >>> test_location.get_enemy().get_name()
        'Monster'
        """
        self.__enemy = enemy

    def get_enemy(self) -> Enemy:
        """
        Get enemy.

        :postcondition: returns object of type Enemy
        :return: an Enemy
        >>> test_location = Location("Hall")
        >>> test_location.set_enemy(Enemy("Monster"))
        >>> test_location.get_enemy().set_description("kind")
        >>> test_location.get_enemy().set_experience(5)
        >>> print(test_location.get_enemy())
        Monster | HP: , Experience: 5, description: kind
        """
        return self.__enemy

    def describe_location(self) -> None:
        """
        Display description.

        :postcondition: produces side effect and prints out description as a string

        >>> test_location = Location("Hall")
        >>> test_location.set_description("test description")
        >>> test_location.describe_location()
        test description
        """
        description = textwrap.fill(self.__description, width=100)
        print(description)

    def __str__(self) -> str:
        """
        Build a string representation of the location object.

        :postcondition: builds a string representation of the location object in the following format
        {self.__location_type}, {self.__description}, {self.__enemy}
        :return: a string

        >>> test_location = Location("Hall")
        >>> test_location.set_description("It has fireplace.")
        >>> test_location.set_enemy(Enemy("Monster"))
        >>> test_location.get_enemy().set_description("kind")
        >>> test_location.get_enemy().set_hp(10)
        >>> test_location.get_enemy().set_experience(5)
        >>> print(test_location)
        Hall| description: It has fireplace., enemy: Monster | HP: 10, Experience: 5, description: kind
        """
        return f'{self.__location_type}| description: {self.__description}, enemy: {self.__enemy}'

    def __repr__(self) -> str:
        """
        Build a string representation of the location object type and state.

        :postcondition: builds a string representation of the location object in the following format
        {self.__class__.__name__}("{self.__location_type}", {self.__description}, {self.__enemy})
        :return: a string

        >>> test_location = Location("Hall")
        >>> test_location.set_description("It has fireplace.")
        >>> test_location.set_enemy(Enemy("Monster"))
        >>> test_location.get_enemy().set_description("kind")
        >>> test_location.get_enemy().set_hp(10)
        >>> test_location.get_enemy().set_experience(5)
        >>> test_location
        Location("Hall", It has fireplace., Monster | HP: 10, Experience: 5, description: kind)
        """
        return f'{self.__class__.__name__}("{self.__location_type}", {self.__description}, {self.__enemy})'
