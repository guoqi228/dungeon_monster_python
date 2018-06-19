class Grid():

    @classmethod
    def make_grid(cls, num_col, num_row, monsters, player, eggs, door, level):
        print('====================================================')
        print('               Welcome to the Dungeon!              ')
        print('====================================================')
        print('Collect all eggs and escape safely through the door!')
        print('====================================================')
        print('        Level: {}                Eggs: {}/{}  '.format(level, player.num_eggs, level))
        print('====================================================')
        #num_col = num_row = level + 4
        col_sep = '|'
        fill = ' ' * 7
        row_padding = col_sep + ' ' * (len(fill))
        row_empty = ' ' * (len(fill))
        row_sep = '-' * (len(fill) + 1)
        for i in range(num_row):
            print(row_sep * num_col)
            print(row_padding * (num_col) + col_sep)
            for j in range(num_col):
                has_monster = False
                has_egg = False
                for monster in monsters:
                    if monster.coords == [i, j]:
                        if j == num_col - 1:
                            print(col_sep + 'Monster' + col_sep, end = '')
                            has_monster = True
                        else:
                            print(col_sep + 'Monster', end = '')
                            has_monster = True
                for egg in eggs:
                    if egg.coords == [i, j] and has_monster == False:
                        if j == num_col - 1:
                            print(col_sep + '  Egg  ' + col_sep, end = '')
                            has_egg = True
                        else:
                            print(col_sep + '  Egg  ', end = '')
                            has_egg = True
                if player.coords == [i, j] and has_monster == False and has_egg == False:
                    if j == num_col - 1:
                        print(col_sep + '  You  ' + col_sep, end = '')
                    else:
                        print(col_sep + '  You  ', end = '')
                elif door.coords == [i, j] and has_monster == False and has_egg == False:
                    if j == num_col - 1:
                        print(col_sep + ' Door  ' + col_sep, end = '')
                    else:
                        print(col_sep + ' Door  ', end = '')
                elif has_monster == False and has_egg == False:
                    if j == num_col - 1:
                        print(col_sep + row_empty + col_sep, end = '')
                    else:
                        print(col_sep + row_empty, end = '')
            print()
            print(row_padding * (num_col) + col_sep)
        print(row_sep * num_col)
