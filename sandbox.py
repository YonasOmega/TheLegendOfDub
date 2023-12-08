from Model.Characters.Monsters.Monster import Monster
from Model.Characters.hero.Warrior import Warrior

hero = Warrior("Hero")
hero.position = (10, 20)
mons = Monster("Mons", 125, 20, 30, 2, 0.8, 0.2)
mons.position = (10, 20)
print("Hero Y Position:", hero.get_y_position())
print("Monster Y Position:", mons.get_y_position())
print("Hero X Position:", hero.get_x_position())
print("Monster X Position:", mons.get_x_position())
print(mons.position)
if mons.get_y_position() == hero.get_y_position() or mons.get_x_position() == hero.get_x_position():
    print(mons.perform_attack(hero))
print(hero.get_health())
