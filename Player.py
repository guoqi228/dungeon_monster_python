class Player():
    def __init__(self, coords = [0, 0], num_eggs = 0):
        self.coords = coords
        self.num_eggs = num_eggs

    def check_egg(self, egg):
        if self.coords == egg.coords:
            self.num_eggs += 1
            egg.coords = [-1, -1]

    def move_player(self, rows, cols):
        move_menu = Menu('Move options', ['Up', 'Down', 'Left', 'Right'])
        move_menu.show_menu()
        print('Where would you like to move?')
        option = UserInput.int_input(0, move_menu.menu_length() - 1)
        if option == 0:
            if self.coords[0] <= 0:
                self.coords = [rows - 1, self.coords[1]]
            else:
                self.coords = [self.coords[0] - 1, self.coords[1]]
        elif option == 1:
            if self.coords[0] >= rows - 1:
                self.coords = [0, self.coords[1]]
            else:
                self.coords = [self.coords[0] + 1, self.coords[1]]
        elif option == 2:
            if self.coords[1] <= 0:
                self.coords = [self.coords[0], cols - 1]
            else:
                self.coords = [self.coords[0], self.coords[1] - 1]
        elif option == 3:
            if self.coords[1] >= cols - 1:
                self.coords = [self.coords[0], 0]
            else:
                self.coords = [self.coords[0], self.coords[1] + 1]

    # create a game over function
    def game_over(self, monsters, door, total_num_eggs):
        for monster in monsters:
            if self.coords == monster.coords:
                return 1
        if self.coords == door.coords and total_num_eggs == self.num_eggs:
            return 2
        return False
