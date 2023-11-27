import sqlite3


#define connection and cursor
connection = sqlite3.connect("monsters.db")

cur = connection.cursor()

# create monster table
monsters = """CREATE TABLE IF NOT EXISTS
monster(monster_type TEXT PRIMARY KEY, health INTEGER, min_damage INTEGER, max_damage INTEGER, attack_speed INTEGER, chance_to_hit NUMERIC, chance_to_heal NUMERIC)"""

cur.execute(monsters)

# Inserting into stores
cur.execute("INSERT INTO monster (monster_type, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal) VALUES ('Ogre', 200, 30, 60, 2, 0.6, 0.1)")
cur.execute("INSERT INTO monster (monster_type, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal) VALUES ('Gremlin', 70, 15, 30, 5, 0.8, 0.4)")
cur.execute("INSERT INTO monster (monster_type, health, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal) VALUES ('Skeleton', 100, 30, 50, 3, 0.8, 0.3)")

#
# # create monster table
# hero = """CREATE TABLE IF NOT EXISTS
# character(hero_type TEXT, health INTEGER, strength INTEGER, speed INTEGER)"""
# cur.execute(hero)
#
# # Inserting into stores
# cur.execute("INSERT INTO character (hero_type, health, strength, speed) VALUES ('Warrior', 6, 3, 3)")
# cur.execute("INSERT INTO character (hero_type, health, strength, speed) VALUES ('Priestess', 10, 2, 2)")
# cur.execute("INSERT INTO character (hero_type, health, strength, speed) VALUES ('Mage', 4, 5, 2)")
# cur.execute("INSERT INTO character (hero_type, health, strength, speed) VALUES ('Thief', 4, 1, 5)")


#get results
cur.execute("SELECT * FROM monster")

results = cur.fetchall()
print(results)
connection.commit()
connection.close()
