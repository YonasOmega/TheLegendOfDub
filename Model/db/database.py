import sqlite3


#define connection and cursor
connection = sqlite3.connect("characters.db")

cur = connection.cursor()

# create monster table
monsters = """CREATE TABLE IF NOT EXISTS
monster(monster_type TEXT, health INTEGER, strength INTEGER, speed INTEGER)"""
cur.execute(monsters)


# Inserting into stores
cur.execute("INSERT INTO monster (monster_type, health, strength, speed) VALUES ('Ogre', 20, 3, 2)")
cur.execute("INSERT INTO monster (monster_type, health, strength, speed) VALUES ('Goblin', 10, 2, 4)")
cur.execute("INSERT INTO monster (monster_type, health, strength, speed) VALUES ('Skeleton', 1, 1, 2)")

# create monster table
hero = """CREATE TABLE IF NOT EXISTS
character(hero_type TEXT, health INTEGER, strength INTEGER, speed INTEGER)"""
cur.execute(hero)

# Inserting into stores
cur.execute("INSERT INTO character (hero_type, health, strength, speed) VALUES ('Warrior', 6, 3, 3)")
cur.execute("INSERT INTO character (hero_type, health, strength, speed) VALUES ('Priestess', 10, 2, 2)")
cur.execute("INSERT INTO character (hero_type, health, strength, speed) VALUES ('Mage', 4, 5, 2)")
cur.execute("INSERT INTO character (hero_type, health, strength, speed) VALUES ('Thief', 4, 1, 5)")


#get results
cur.execute("SELECT * FROM monster")

results = cur.fetchall()
print(results)
connection.commit()
connection.close()
