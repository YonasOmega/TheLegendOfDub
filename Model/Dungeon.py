from Model.DungeonGenerator import DungeonGenerator


class Dungeon():

    def __init__(self):
        self.dungeon = DungeonGenerator(5, 5)
        self.dungeon_file = self.read_dungeon_from_file("Dungeon.txt")
        self.dungeon_layout = self.parse_dungeon()

    def read_dungeon_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip().split() for line in lines]

    def parse_dungeon(self):
        return [list(line) for line in self.dungeon_file if line]

    # Room Builders and get_room_visual method remain the same

    # Override __str__ method
    def __str__(self):
        dungeon_visual = "X" * (4 * len(self.dungeon_layout[0]) + 1) + "\n"

        for i, row in enumerate(self.dungeon_layout):
            room_line = "|"
            path_line = "X"
            for j, cell in enumerate(row):
                if cell in ['P', 'Y', 'I', 'E', 'A', 'X']:
                    room_line += f" {cell} |"
                elif cell == '1':
                    room_line += "   |"
                else:  # cell == '0'
                    room_line += "    "

                if j < len(row) - 1:
                    if row[j] == '1' or row[j + 1] == '1':
                        path_line += "----X"
                    else:
                        path_line += "XXXXX"
                else:
                    path_line += "X"

            dungeon_visual += room_line + "\n"
            if i < len(self.dungeon_layout) - 1:
                dungeon_visual += path_line + "\n"
            else:
                dungeon_visual += "X" * (4 * len(row) + 1) + "\n"

        return dungeon_visual

# Rest of the Dungeon class remains the same

# Example usage
dun = Dungeon()
print(dun)

