"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
from prettytable import PrettyTable


class Enemy:

    def __init__(self, name):
        self.__enemy_name = name
        self.__description = "description"
        self.__hp = ""
        self.__experience = ""

    def get_name(self):
        return self.__enemy_name

    def set_description(self, description):
        self.__description = description

    def set_hp(self, hp):
        self.__hp = hp

    def get_hp(self):
        return self.__hp

    def set_experience(self, experience):
        self.__experience = experience

    def get_experience(self):
        return self.__experience

    def change_hp(self, damage):
        self.__hp += damage

    def show_enemy_stat(self):
        headers = ["Enemy", "HP", "Experience"]
        info = [self.__name, self.__hp, self.__experience]
        table = PrettyTable(headers)
        table.add_row(info)
        print(table)

    def describe_enemy(self):
        print(self.__description)

    def __str__(self):
        return f'{self.__enemy_name}, {self.__description}, {self.__hp}, {self.__experience}'
