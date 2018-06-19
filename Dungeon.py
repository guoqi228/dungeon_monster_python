class Dungeon():

    level = 0
    exit = False
    while not exit:

        level += 1
        all_objects = []
        player = Player()
        door = Door()
        monsters = [Monster([0, 0]) for i in range(level)]
        eggs = [Egg([0, 0]) for i in range(level)]
        all_objects = [player, door] + monsters + eggs

        cols = rows = level + 4
        all_coords = []
        for i in range(rows):
            for j in range(cols):
                all_coords.append([i, j])

        indice = np.random.choice(cols * rows - 1, level * 2 + 2, replace = False)

        for i, index in enumerate(indice):
            all_objects[i].coords = all_coords[index]

        is_over = False
        while not is_over:

            clear_output()
            Grid.make_grid(rows, cols, monsters, player, eggs, door, level)
            player.move_player(rows, cols)
            for egg in eggs:
                player.check_egg(egg)
            for monster in monsters:
                boolean_list = monster.check_nearby(rows, cols, eggs, door, monsters)
                monster.move_monster(rows, cols, player, boolean_list)
            # check game_over
            flag = player.game_over(monsters, door, level)
            if flag == 1:
                clear_output()
                Grid.make_grid(rows, cols, monsters, player, eggs, door, level)
                print('You lost! The monster got you!')
                level -= 1
                is_over = True
                break
            elif flag == 2:
                clear_output()
                Grid.make_grid(rows, cols, monsters, player, eggs, door, level)
                print('Congratulation! You win!')
                is_over = True
                break
        print('Continue to play?')
        ans = UserInput.yes_input()
        #ans = str(input('Would you like to play again?y or n: '))
        if ans == False:
            exit = True
            print('Exiting the game...')
            print('Bye!')
            break
