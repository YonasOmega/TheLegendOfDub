from Model.Characters.hero.Heroes import Hero
from Model.Characters.DungeonCharacter import DungeonCharacter


class Priestess(Hero):
    def __init__(self, name):
        super().__init__(name, health=75, min_damage=50, max_damage=100, attack_speed=2, chance_to_hit=0.7, chance_to_block=0.1)

    def special_skill(self, target: DungeonCharacter):
        # Implement the fireball special skill
        fireball = self.calculate_damage() * 1.5
        target.receive_damage(fireball)
        return f"{self._name} used fireball on {target.name}, dealing {fireball} hit points."

# Example usage:
# priestess = Priestess("PriestessName")

