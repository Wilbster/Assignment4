"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
from control import get_player_choice


def execute_combat_magic(character, enemy):
    spells = ('Fireball', 'Heal')
    number_of_spells = len(spells)
    options = enumerate(spells, 1)
    print('Choose a spell.')
    choice = get_player_choice(options)
    if choice == 'Fireball':
        if mana_drain(character):
            level = character.get_level()
            damage = 3*level**2
            enemy.change_hp(-damage)
            print(f"A giant fireball bursts forth from the palms of your hands, doing {damage} points of damage"
                  f"to the enemy!")
            print(f"The enemy now has {enemy.get} ")
    if choice == 'Heal':
        if mana_drain(character):
            max_hp = character.get_max_hp()
            character.set_current_hp(max_hp)
            print(f"You have used the mystic arts to heal yourself fully! You now have {max_hp} HP left!")


def mana_drain(character):
    if character.get_current_mana() > 0:
        character.change_current_mana(-1)
        current_mana = character.get_current_mana()
        print(f"You lose 1 mana point. You now have {current_mana} mana points left.")
        return True
    else:
        print('Alas, you are out of mana!')
        return False






def main():
    pass


if __name__ == '__main__':
    main()