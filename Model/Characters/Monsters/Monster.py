from abc import ABC
import sqlite3

from Model.Characters.DungeonCharacter import DungeonCharacter
import random
import os


class Monster(DungeonCharacter, ABC):
    def __init__(self, name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal):
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit)
        # self._position = (0,0)
        self.__chance_to_heal = chance_to_heal

    @property
    def chance_to_heal(self):
        return self.__chance_to_heal

    @chance_to_heal.setter
    def chance_to_heal(self, value):
        self.__chance_to_heal = value


    def heal(self):
        # A Monster has a chance to heal after any attack that causes a loss of hit points
        # The chance to heal is checked after the Monster has been attacked and hit points have been lost
        if self.is_alive() and random.random() < self.__chance_to_heal:
            heal_amount = random.randint(15, 30)  # Adjust the healing range as needed
            self.set_health(heal_amount)
            print(f"{self.get_name()} healed itself for {heal_amount} hit points.")

    def attack(self, opponent):
        if self.can_attack():
            damage = random.randint(self.min_damage, self.max_damage)
            print(f"{self.get_name()} attacked {opponent.get_name()} for {damage} damage.")
            opponent.receive_damage(damage)
            self.heal()
        else:
            print(f"{self.get_name()} missed the attack on {opponent.get_name()}.")


class Gremlin(Monster):
    def __init__(self):
        gremlin_data = Gremlin.fetch_gremlin_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = gremlin_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)

    @staticmethod
    def fetch_gremlin_data():
        db_path = os.path.join(os.path.dirname(os.getcwd()), "Model", "db", "monsters.db")
        try:
            connection = sqlite3.connect(db_path)
        except sqlite3.OperationalError as e:
            print(f"Error opening database: {e}")
            return None

        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM monster WHERE monster_type = 'Gremlin'")
            monster_data = cur.fetchone()
        except sqlite3.OperationalError as e:
            print(f"Error querying database: {e}")
            monster_data = None

        connection.close()
        return monster_data


class Skeleton(Monster):
    def __init__(self):
        skeleton_data = Skeleton.fetch_skeleton_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = skeleton_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)

    @staticmethod
    def fetch_skeleton_data():
        db_path = os.path.join(os.path.dirname(os.getcwd()), "Model", "db", "monsters.db")
        try:
            connection = sqlite3.connect(db_path)
        except sqlite3.OperationalError as e:
            print(f"Error opening database: {e}")
            return None

        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM monster WHERE monster_type = 'Skeleton'")
            monster_data = cur.fetchone()
        except sqlite3.OperationalError as e:
            print(f"Error querying database: {e}")
            monster_data = None

        connection.close()
        return monster_data


class Ogre(Monster):
    def __init__(self):
        ogre_data = Ogre.fetch_ogre_data()
        name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal = ogre_data
        super().__init__(name, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal)

    @staticmethod
    def fetch_ogre_data():
        db_path = os.path.join(os.path.dirname(os.getcwd()), "Model", "db", "monsters.db")
        try:
            connection = sqlite3.connect(db_path)
        except sqlite3.OperationalError as e:
            print(f"Error opening database: {e}")
            return None

        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM monster WHERE monster_type = 'Ogre'")
            monster_data = cur.fetchone()
        except sqlite3.OperationalError as e:
            print(f"Error querying database: {e}")
            monster_data = None

        connection.close()
        return monster_data
