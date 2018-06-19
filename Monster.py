class Monster():
    def __init__(self, coords = [0, 0]):
        self.coords = coords

    def init_coords(self, rows, cols):
        self.coords = [random.randint(0, cols - 1), random.randint(0, rows - 1)]

    def check_nearby(self, rows, cols, eggs, door, monsters):
        go_up = True
        go_down = True
        go_left = True
        go_right = True

        for monster in monsters:
            if [self.coords[0] + 1, self.coords[1]] == [monster.coords[0], monster.coords[1]]:
                go_down = False
            elif [self.coords[0] - 1, self.coords[1]] == [monster.coords[0], monster.coords[1]]:
                go_up = False
            elif [self.coords[0], self.coords[1] + 1] == [monster.coords[0], monster.coords[1]]:
                go_right = False
            elif [self.coords[0], self.coords[1] - 1] == [monster.coords[0], monster.coords[1]]:
                go_left = False
        for egg in eggs:
            if [self.coords[0] + 1, self.coords[1]] == [egg.coords[0], egg.coords[1]]:
                go_down = False
            elif [self.coords[0] - 1, self.coords[1]] == [egg.coords[0], egg.coords[1]]:
                go_up = False
            elif [self.coords[0], self.coords[1] + 1] == [egg.coords[0], egg.coords[1]]:
                go_right = False
            elif [self.coords[0], self.coords[1] - 1] == [egg.coords[0], egg.coords[1]]:
                go_left = False
        if [self.coords[0] + 1, self.coords[1]] == [door.coords[0], door.coords[1]]:
            go_down = False
        elif [self.coords[0] - 1, self.coords[1]] == [door.coords[0], door.coords[1]]:
            go_up = False
        elif [self.coords[0], self.coords[1] + 1] == [door.coords[0], door.coords[1]]:
            go_right = False
        elif [self.coords[0], self.coords[1] - 1] == [door.coords[0], door.coords[1]]:
            go_left = False
        # check boundary
        if self.coords[0] == rows - 1:
            go_down = False
        elif self.coords[0] == 0:
            go_up = False
        elif self.coords[1] == cols - 1:
            go_right = False
        elif self.coords[1] == 0:
            go_left = False
        return [go_up, go_down, go_left, go_right]

    def move_monster(self, rows, cols, player, boolean_list):
        [go_up, go_down, go_left, go_right] = boolean_list
        row_diff = self.coords[0] - player.coords[0]
        col_diff = self.coords[1] - player.coords[1]
        if row_diff > 0 and col_diff == 0 and go_up == True and self.coords[0] - 1 >= 0:
            self.coords = [self.coords[0] - 1, self.coords[1]]
        elif row_diff < 0 and col_diff == 0 and go_down == True and self.coords[0] + 1 <= rows - 1:
            self.coords = [self.coords[0] + 1, self.coords[1]]
        elif row_diff == 0 and col_diff > 0 and go_left == True and self.coords[1] - 1 >= 0:
            self.coords = [self.coords[0], self.coords[1] - 1]
        elif row_diff == 0 and col_diff < 0 and go_right == True and self.coords[1] + 1 <= cols - 1:
            self.coords = [self.coords[0], self.coords[1] + 1]
        elif abs(row_diff) <= abs(col_diff) and row_diff > 0 and go_up == True and self.coords[0] - 1 >= 0:
            self.coords = [self.coords[0] - 1, self.coords[1]]
        elif abs(row_diff) <= abs(col_diff) and row_diff < 0 and go_down == True and self.coords[0] + 1 <= rows - 1:
            self.coords = [self.coords[0] + 1, self.coords[1]]
        elif abs(row_diff) >= abs(col_diff) and col_diff > 0 and go_left == True and self.coords[1] - 1 >= 0:
            self.coords = [self.coords[0], self.coords[1] - 1]
        elif abs(row_diff) >= abs(col_diff) and col_diff < 0 and go_right == True and self.coords[1] + 1 <= cols - 1:
            self.coords = [self.coords[0], self.coords[1] + 1]
        elif go_up == True and rows - 1 > self.coords[0] > (rows - 1)//2:
            self.coords = [self.coords[0] + 1, self.coords[1]]
        elif go_down == True and 0 < self.coords[0] < (rows -1) // 2:
            self.coords = [self.coords[0] - 1, self.coords[1]]
        elif go_left == True and cols - 1 > self.coords[1] > (cols - 1)//2:
            self.coords = [self.coords[0], self.coords[1] - 1]
        elif go_right == True and 0 < self.coords[1] < (cols - 1)//2:
            self.coords = [self.coords[0], self.coords[1] + 1]
        elif go_up == True and self.coords[0] - 1 >= 0:
            self.coords = [self.coords[0] - 1, self.coords[1]]
        elif go_down == True and self.coords[0] + 1 <= rows - 1:
            self.coords = [self.coords[0] + 1, self.coords[1]]
        elif go_left == True and self.coords[1] - 1 >= 0:
            self.coords = [self.coords[0], self.coords[1] - 1]
        elif go_right == True and self.coords[1] + 1 <= cols - 1:
            self.coords = [self.coords[0], self.coords[1] + 1]
