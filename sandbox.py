from Model.Characters.Monsters.Monster import Gremlin
from Model.Characters.Monsters.Monster import Skeleton
from Model.Characters.hero.Warrior import Warrior
from Model.Characters.hero.Thief import Thief
from Model.Characters.hero.Priestess import Priestess
from Model.rooms.Items.potion.Health_Potion import Health_Potion
from Model.rooms.Items.Pillar.OOP import Abstraction
from Model.rooms.Items.Pillar.OOP import Polymorphism
from Model.rooms.Items.Pillar.OOP import Encapsulation
from Model.rooms.Items.Pillar.OOP import Inheritance
from Model.Characters.Monsters.Monster import Ogre
from Model.Characters.Monsters.Monster import Monster
from Model.Characters import Combat_Encounter

warrior = Warrior("Warrior")
# thief = Thief("Thief")
# priest = Priestess("Priest")
#
# warrior_mon1 = Monster("Ogre", 200, 50, 60, 2, 0.6, 0.1)
#
# while warrior_mon1.get_health() > 0:
#     warrior.attack(warrior_mon1)
#     print(warrior_mon1)
#
# warrior_mon1 = Monster("Ogre", 200, 50, 60, 2, 0.6, 0.1)
#
# while warrior_mon1.get_health() > 0:
#     warrior.special_skill(warrior_mon1)
#     print(warrior_mon1)
#
# # warrior_mon1 = Monster("Ogre", 200, 1, 1, 3, 1.0, 0.1)
# # Combat_Encounter.start_combat(warrior, warrior_mon1)
#
# warrior_mon1 = Monster("Ogre", 200, 50, 60, 2, 0.6, 0.1)
#
# while warrior_mon1.get_health() > 0:
#     thief.attack(warrior_mon1)
#     print(warrior_mon1)
# print("NExt")
#
# warrior_mon1 = Monster("Ogre", 200, 50, 60, 2, 0.6, 0.1)
#
# while warrior_mon1.get_health() > 0:
#     thief.special_skill(warrior_mon1)
#     print(warrior_mon1)
#
# warrior_mon1 = Monster("Ogre", 200, 50, 60, 2, 0.6, 0.1)
#
# while warrior_mon1.get_health() > 0:
#     priest.attack(warrior_mon1)
#     print(warrior_mon1)
# print("NExt")
#
# warrior_mon1 = Monster("Ogre", 200, 50, 60, 2, 0.6, 0.1)
# priest.I_want_to_lose()
#
# while priest.get_health() < 75:
#     priest.special_skill(warrior_mon1)
#     print(priest)
#     print(warrior_mon1)
potion = Health_Potion()
warrior.put_in_bag(potion)
warrior.use_item(1)




