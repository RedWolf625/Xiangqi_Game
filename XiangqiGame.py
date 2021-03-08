# Author: Nathan Shelby
# Date: 3/11/20
# Description: Create a working digital version of the game Xiangqi


# Create a class called XiangqiGame that initializes a board (which is a list of lists), a move counter to see whose
# Turn it is, the game state, and the check status of both players.
# The board has the shortened string of the color and type of every piece.
class XiangqiGame:
    def __init__(self):
        self.__move_counter = 0
        self.__game_state = 'UNFINISHED'
        self.__black_check = 'NOT IN CHECK'
        self.__red_check = 'NOT IN CHECK'
        self.__board = [['  '], ['a '], ['b '], ['c '], ['d '], ['e '], ['f '], ['g '], ['h '], ['i '],
                        ['10'], ['BC'], ['BH'], ['BE'], ['BA'], ['BG'], ['BA'], ['BE'], ['BH'], ['BC'],
                        ['9'], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '],
                        ['8'], ['  '], ['BN'], ['  '], ['  '], ['  '], ['  '], ['  '], ['BN'], ['  '],
                        ['7'], ['BS'], ['  '], ['BS'], ['  '], ['BS'], ['  '], ['BS'], ['  '], ['BS'],
                        ['6'], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '],
                        ['5'], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '],
                        ['4'], ['RS'], ['  '], ['RS'], ['  '], ['RS'], ['  '], ['RS'], ['  '], ['RS'],
                        ['3'], ['  '], ['RN'], ['  '], ['  '], ['  '], ['  '], ['  '], ['RN'], ['  '],
                        ['2'], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '],
                        ['1'], ['RC'], ['RH'], ['RE'], ['RA'], ['RG'], ['RA'], ['RE'], ['RH'], ['RC']]

    # Create a function that handles the horse movement.  It takes the current sub-list number and the destination
    # Sub-list number from the make_move function and moves the horse piece to the destination if it is a valid move.
    def horse_move(self, loc, dest):
        # Initialize a variable to hold the board, a variable to hold the current location,
        # a variable to hold the destination, a variable that is the difference of the two, and a list of viable moves.
        board = self.__board
        spot_h = loc
        destination = dest
        combo_numb = destination - spot_h
        viable_moves = [8, -8, 12, -12, 19, -19, 21, -21]
        # Check to see if the destination is one of the 8 valid spots that the horse can move to from the current spot.
        # If not, print the error and return.
        if combo_numb not in viable_moves:
            raise NotALegalMove
        # Split the string of the destination and current sub-list and see if the first character in that sub-list are
        # The same.  If they are, raise an error.
        dest_char = [char for char in board[destination][0]]
        cur_char = [char for char in board[spot_h][0]]
        if dest_char[0] == cur_char[0]:
            raise NotALegalMove
        # Check to see if there is a piece in the way of the horse moving backwards.  If so, raise an error.
        if destination == spot_h - 19:
            horse_check = spot_h - 10
            if board[horse_check] != ['  ']:
                raise NotALegalMove
        # Check to see if there is a piece in the way of the horse moving forward.  If so, raise an error.
        if destination == spot_h + 19:
            horse_check = spot_h + 10
            if board[horse_check] != ['  ']:
                raise NotALegalMove
        # Check to see if there is a piece in the way of the horse moving forward.  If so, raise an error.
        if destination == spot_h + 21:
            horse_check = spot_h + 10
            if board[horse_check] != ['  ']:
                raise NotALegalMove
        # Check to see if there is a piece in the way of the horse moving backwards.  If so, raise an error.
        if destination == spot_h - 21:
            horse_check = spot_h - 10
            if board[horse_check] != ['  ']:
                raise NotALegalMove
        # Check to see if there is a piece in the way of the horse moving left.  If so, raise an error.
        if destination == spot_h - 8:
            horse_check = spot_h + 1
            if board[horse_check] != ['  ']:
                raise NotALegalMove
        # Check to see if there is a piece in the way of the horse moving right.  If so, raise an error.
        if destination == spot_h + 8:
            horse_check = spot_h - 1
            if board[horse_check] != ['  ']:
                raise NotALegalMove
        # Check to see if there is a piece in the way of the horse moving right.  If so, raise an error.
        if destination == spot_h + 12:
            horse_check = spot_h + 1
            if board[horse_check] != ['  ']:
                raise NotALegalMove
        # Check to see if there is a piece in the way of the horse moving left.  If so, raise an error.
        if destination == spot_h - 12:
            horse_check = spot_h - 1
            if board[horse_check] != ['  ']:
                raise NotALegalMove
        # If all the checks have passed, return true
        return True

    # Create a function that handles the elephant movement.  It takes the current sub-list number and the destination
    # Sub-list number from the make_move function and moves the elephant piece to the destination if it is a valid move.
    def elephant_move(self, loc, dest):
        # Initialize a variable to hold the river values, the board, the current sub-list location, the destination
        # Sub-list location, a variable to hold the difference between the two, and a list of viable moves
        river = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
                 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
        board = self.__board
        spot_e = loc
        destination = dest
        combo_num = destination - spot_e
        viable_moves = [18, -18, 22, -22]
        # Check to see if the destination value is one of the 4 viable moves.  If not, it prints an error and returns.
        if combo_num not in viable_moves:
            raise NotALegalMove
        # Check to see if there is a piece in the way of the elephant moving backwards.
        # If so, raise an error.
        if destination == spot_e - 18:
            eleph_check = spot_e - 9
            if board[eleph_check] != ['  ']:
                raise NotALegalMove
        # Check to see if there is a piece in the way of the elephant moving forwards.
        # If so, raise an error.
        if destination == spot_e + 18:
            eleph_check = spot_e + 9
            if board[eleph_check] != ['  ']:
                raise NotALegalMove
        # Check to see if there is a piece in the way of the elephant moving forwards.
        # If so, raise an error.
        if destination == spot_e + 22:
            eleph_check = spot_e + 11
            if board[eleph_check] != ['  ']:
                raise NotALegalMove
        # Check to see if there is a piece in the way of the elephant moving backwards.
        # If so, raise an error.
        if destination == spot_e - 22:
            eleph_check = spot_e - 11
            if board[eleph_check] != ['  ']:
                raise NotALegalMove
        # Split the string of the destination and current sub-list and see if the first character in that sub-list are
        # The same.  If they are, raise an error.
        dest_char = [char for char in board[destination][0]]
        cur_char = [char for char in board[spot_e][0]]
        if dest_char[0] == cur_char[0]:
            raise NotALegalMove
        # Check to see if the elephant has tried to cross the river.  If so, raise an error
        if spot_e < 60:
            if destination > 60:
                raise NotALegalMove
        if spot_e > 59:
            if destination < 59:
                raise NotALegalMove
        # If all the checks have passed, return true
        return True

    # Create a function that handles the chariot movement.  It takes the current sub-list number and the destination
    # Sub-list number from the make_move function and moves the horse piece to the destination if it is a valid move.
    def chariot_move(self, loc, dest):
        # Initialize a variable to hold the board, the current sub-list location, the destination
        # Sub-list location, the difference between the two, and a list of viable moves
        board = self.__board
        destination = dest
        spot_c = loc
        combo_num = destination - spot_c
        valid_moves = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 1, -1, 2, -2, 3,
                       -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]
        # Check to see if the destination is one of the viable moves for the chariot.  If not, raise an error
        if combo_num not in valid_moves:
            raise NotALegalMove
        # If the destination is within the range of 0-10, ensure that the chariot doesn't move to a new row
        # Laterally by splitting the string of the current spot and the destination spot.  Compare the first number of
        # That string and ensure that they are the same.  If not, raise an error
        row_check = destination - spot_c
        if 0 < row_check < 10:
            str_spot = [char for char in str(spot_c)[0]]
            str_dest = [char for char in str(destination)[0]]
            if str_spot != str_dest:
                raise NotALegalMove
            # Check to see if there is a piece between the chariot and the destination.
            # If so, raise an error
            test = spot_c + 1
            test_2 = destination - 1
            if test_2 > test:
                for x in range(spot_c + 1, destination):
                    if board[x] != ['  ']:
                        raise NotALegalMove
            if test == test_2:
                if board[test] != ['  ']:
                    raise NotALegalMove
        # If the destination is within the range of 0-(-10), ensure that the chariot doesn't move to a new row
        # Laterally by splitting the string of the current spot and the destination spot.  Compare the first number of
        # That string and ensure that they are the same.  If not, raise an error
        if 0 > row_check > - 10:
            str_spot = [char for char in str(spot_c)[0]]
            str_dest = [char for char in str(destination)[0]]
            if str_spot != str_dest:
                raise NotALegalMove
            # Check to see if there is a piece between the chariot and the destination.
            # If so, raise an error
            test = spot_c - 1
            test_2 = destination + 1
            if test_2 < test:
                for x in range(destination + 1, spot_c):
                    if board[x] != ['  ']:
                        raise NotALegalMove
            if test == test_2:
                if board[test] != ['  ']:
                    raise NotALegalMove
        # Split the string of the destination and current sub-list and see if the first character in that sub-list are
        # The same.  If they are, raise an error.
        if board[destination] != ['  ']:
            dest_char = [char for char in board[destination][0]]
            cur_char = [char for char in board[spot_c][0]]
            if dest_char[0] == cur_char[0]:
                raise NotALegalMove
        if combo_num % 10 == 0:
            if combo_num > 0:
                str_combo = [char for char in str(combo_num)]
                fin_str = int(str_combo[0])
                if fin_str > 1:
                    for x in range(1, fin_str):
                        y = 10 * x
                        if board[spot_c + y] != ['  ']:
                            raise NotALegalMove
            if combo_num < 0:
                str_combo = [char for char in str(combo_num)]
                fin_str = int(str_combo[1])
                if fin_str > 1:
                    for x in range(1, fin_str):
                        y = -10 * x
                        if board[spot_c + y] != ['  ']:
                            raise NotALegalMove
        # If all the checks have passed, return true
        return True

    # Create a function that handles the cannon movement.  It takes the current sub-list number and the destination
    # Sub-list number from the make_move function and moves the horse piece to the destination if it is a valid move.
    def cannon_move(self, counter, loc, dest):
        # Initialize a variable to hold the board, the current sub-list location, the destination
        # Sub-list location, the difference between the two, and a list of viable moves
        board = self.__board
        destination = dest
        spot_n = loc
        combo_num = destination - spot_n
        cannon_jump = 0
        loop_counter = counter
        valid_moves = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 1, -1, 2, -2, 3,
                       -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]

        # Check to see if the destination is one of the viable moves for the cannon.  If not, raise an error
        if combo_num not in valid_moves:
            raise NotALegalMove
        # If the destination is within the range of 0-10, ensure that the chariot doesn't move to a new row
        # Laterally by splitting the string of the current spot and the destination spot.  Compare the first number of
        # That string and ensure that they are the same.  If not, raise an error
        row_check = destination - spot_n
        if 0 < row_check < 10:
            str_spot = [char for char in str(spot_n)[0]]
            str_dest = [char for char in str(destination)[0]]
            if str_spot != str_dest:
                raise NotALegalMove
            # Create a counter and count the number of occupied spaces between the destination and the current spot.
            # If it is more than 1, raise an error, if it's 0, raise an error.
            test = spot_n + 1
            test_2 = destination - 1
            if test_2 > test:
                if loop_counter == 2:
                    pass
                if board[destination] != ['  '] or loop_counter == 1:
                    for x in range(spot_n + 1, destination):
                        if board[x] != ['  ']:
                            cannon_jump += 1
                    if cannon_jump > 1:
                        raise NotALegalMove
                    if cannon_jump == 0:
                        raise NotALegalMove
            if test == test_2:
                if board[test] == ['  ']:
                    raise NotALegalMove
        # If the destination is within the range of 0-(-10), ensure that the chariot doesn't move to a new row
        # Laterally by splitting the string of the current spot and the destination spot.  Compare the first number of
        # That string and ensure that they are the same.  If not, raise an error
        if 0 > row_check > - 10:
            str_spot = [char for char in str(spot_n)[0]]
            str_dest = [char for char in str(destination)[0]]
            if str_spot != str_dest:
                raise NotALegalMove
            # Create a counter and count the number of occupied spaces between the destination and the current spot.
            # If it is more than 1, raise an error, if it's 0, raise an error.
            test = spot_n - 1
            test_2 = destination + 1
            if test_2 < test:
                if loop_counter == 2:
                    pass
                if board[destination] != ['  '] or loop_counter == 1:
                    for x in range(destination + 1, spot_n):
                        if board[x] != ['  ']:
                            cannon_jump += 1
                    if cannon_jump > 1:
                        raise NotALegalMove
                    if cannon_jump == 0:
                        raise NotALegalMove
            if test == test_2:
                if board[test] == ['  ']:
                    raise NotALegalMove
        if combo_num % 10 == 0:
            if loop_counter == 2:
                pass
            if board[destination] != ['  '] or loop_counter == 1:
                if combo_num > 0:
                    str_combo = [char for char in str(combo_num)]
                    fin_str = int(str_combo[0])
                    if fin_str == 1:
                        raise NotALegalMove
                    if fin_str > 1:
                        for x in range(1, fin_str):
                            y = 10 * x
                            if board[spot_n + y] != ['  ']:
                                cannon_jump += 1
                        if cannon_jump > 1:
                            raise NotALegalMove
                        if cannon_jump == 0:
                            raise NotALegalMove
                if combo_num < 0:
                    str_combo = [char for char in str(combo_num)]
                    fin_str = int(str_combo[1])
                    if fin_str == 1:
                        raise NotALegalMove
                    if fin_str > 1:
                        for x in range(1, fin_str):
                            y = -10 * x
                            if board[spot_n + y] != ['  ']:
                                cannon_jump += 1
                        if cannon_jump > 1:
                            raise NotALegalMove
                        if cannon_jump == 0:
                            raise NotALegalMove
        # Split the string of the destination and current sub-list and see if the first character in that sub-list are
        # The same.  If they are, raise an error.
        if board[destination] != ['  ']:
            dest_char = [char for char in board[destination][0]]
            cur_char = [char for char in board[spot_n][0]]
            if dest_char[0] == cur_char[0]:
                raise NotALegalMove
        # If all the checks have passed, return True
        return True

    # Create a function that handles the soldier movement.  It takes the current sub-list number and the destination
    # Sub-list number from the make_move function and moves the horse piece to the destination if it is a valid move.
    def soldier_move(self, loc, dest):
        # Initialize a variable to hold the river values, the board, the current sub-list location, the destination
        # Sub-list location, the difference between the two, and a list of viable moves
        river = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
                 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
        board = self.__board
        spot_s = loc
        destination = dest
        combo_num = destination - spot_s
        viable_moves = [1, -1, 10, -10]
        # Check to see if the movement we are expected to do is viable
        if combo_num not in viable_moves:
            raise NotALegalMove

        # Split the string of the destination and current sub-list and see if the first character in that sub-list are
        # The same.  If they are, raise an error.
        dest_char = [char for char in board[destination][0]]
        cur_char = [char for char in board[spot_s][0]]
        if dest_char[0] == cur_char[0]:
            raise NotALegalMove
        # Check to see if the soldier has crossed the river and thus can move sideways.
        # If not and we are expected to move sideways, raise an error
        if cur_char[0] == 'B':
            if spot_s < 60:
                combo_num = destination - spot_s
                if combo_num % 10 != 0:
                    raise NotALegalMove
            if destination == spot_s - 10:
                raise NotALegalMove
        if cur_char[0] == 'R':
            if spot_s > 59:
                combo_num = destination - spot_s
                if combo_num % 10 != 0:
                    raise NotALegalMove
            if destination == spot_s + 10:
                raise NotALegalMove
        # If all the tests have passed, return true
        return True

    # Create a function that handles the advisor movement.  It takes the current sub-list number and the destination
    # Sub-list number from the make_move function and moves the horse piece to the destination if it is a valid move.
    def advisor_move(self, loc, dest):
        # Initialize a variable to hold the palace values, the board, the current sub-list location, the destination
        # Sub-list location, the difference between the two, and a list of viable moves
        palace = [14, 15, 16, 24, 25, 26, 34, 35, 36, 84, 85, 86, 94, 95, 96, 104, 105, 106]
        board = self.__board
        spot_a = loc
        destination = dest
        combo_num = destination - spot_a
        viable_moves = [9, -9, 11, -11]
        # Check to see if the destination is one of the viable moves for the advisor.  If not, raise an error
        if combo_num not in viable_moves:
            raise NotALegalMove
        # Split the string of the destination and current sub-list and see if the first character in that sub-list are
        # The same.  If they are, raise an error.
        dest_char = [char for char in board[destination][0]]
        cur_char = [char for char in board[spot_a][0]]
        if dest_char[0] == cur_char[0]:
            raise NotALegalMove
        # Check to see if the destination value is in the palace value list.  If not, raise an error
        if destination not in palace:
            raise NotALegalMove
        # If all the checks have passed, put the string in the current sub-list into a variable, make the current
        # sublist 'empty', and make the destination sub-list hold the piece.
        return True

    # Create a function that handles the general movement.  It takes the current sub-list number and the destination
    # Sub-list number from the make_move function and moves the horse piece to the destination if it is a valid move.
    def general_move(self, counter, loc, dest):
        # Initialize a variable to hold the palace values, the board, the current sub-list location, the destination
        # Sub-list location, lists of all the viable moves of all the pieces that can take the general, and a loop
        # Counter that is used later to run tests to see if the general has any viable moves left.
        soldier_moves = [1, -1, 10, -10]
        general_moves = [1, -1, 10, -10, 70, -70, 80, -80, 90, -90]
        cannon_moves = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 1, -1, 2, -2,
                        3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]
        horse_moves = [8, -8, 12, -12, 19, -19, 21, -21]
        palace = [14, 15, 16, 24, 25, 26, 34, 35, 36, 84, 85, 86, 94, 95, 96, 104, 105, 106]
        board = self.__board
        destination = dest
        spot_g = loc
        move_counter = self.__move_counter
        loop_counter = counter
        combo_num = destination - spot_g
        # Check to see if the destination is one of the viable moves for the general.  If not, raise an error
        if combo_num not in general_moves:
            raise NotALegalMove
        # Split the string of the destination and current sub-list and see if the first character in that sub-list are
        # The same.  If they are, raise an error.
        dest_char = [char for char in board[destination][0]]
        cur_char = [char for char in board[spot_g][0]]
        if dest_char[0] == cur_char[0]:
            raise NotALegalMove
        # For the flying general move, check to see if the spaces between the generals are empty.  If they are not,
        # raise an error
        if destination == spot_g + 70:
            if dest_char[1] == 'G' or loop_counter == 1:
                for x in range(1, 8):
                    y = x * 10
                    if board[spot_g + y] != ['  ']:
                        raise NotALegalMove
        if destination == spot_g - 70:
            if dest_char[1] == 'G' or loop_counter == 1:
                for x in range(1, 8):
                    y = x * -10
                    if board[spot_g + y] != ['  ']:
                        raise NotALegalMove
        if destination == spot_g + 80:
            if dest_char[1] == 'G' or loop_counter == 1:
                for x in range(1, 8):
                    y = x * 10
                    if board[spot_g + y] != ['  ']:
                        raise NotALegalMove
        if destination == spot_g - 80:
            if dest_char[1] == 'G' or loop_counter == 1:
                for x in range(1, 8):
                    y = x * -10
                    if board[spot_g + y] != ['  ']:
                        raise NotALegalMove
        if destination == spot_g + 90:
            if dest_char[1] == 'G' or loop_counter == 1:
                for x in range(1, 8):
                    y = x * 10
                    if board[spot_g + y] != ['  ']:
                        raise NotALegalMove
        if destination == spot_g - 90:
            if dest_char[1] == 'G' or loop_counter == 1:
                for x in range(1, 8):
                    y = x * -10
                    if board[spot_g + y] != ['  ']:
                        raise NotALegalMove
        # Check to see if the destination value is in the palace value list.  If not, raise an error
        if destination not in palace:
            raise NotALegalMove
        # Check to see who's turn it is.  Take the destination spot and see if any of the opposing team's pieces will
        # Be able to reach that spot next turn.  If so, raise an error.  If not, continue
        if move_counter % 2 == 0:
            b = destination
            for z in soldier_moves:
                try:
                    if board[b + z] == ['BS']:
                        try:
                            if XiangqiGame.soldier_move(self, loc=b + z, dest=b):
                                raise GeneralCheck
                        except NotALegalMove:
                            continue
                        except GeneralCheck:
                            raise NotALegalMove
                except IndexError:
                    continue
            for z in cannon_moves:
                try:
                    if board[b + z] == ['BN']:
                        try:
                            if XiangqiGame.cannon_move(self, 1, loc=b + z, dest=b):
                                raise GeneralCheck
                        except NotALegalMove:
                            continue
                        except GeneralCheck:
                            raise NotALegalMove
                except IndexError:
                    continue
                try:
                    if board[b + z] == ['BC']:
                        try:
                            if XiangqiGame.chariot_move(self, loc=b + z, dest=b):
                                raise GeneralCheck
                        except NotALegalMove:
                            continue
                        except GeneralCheck:
                            raise NotALegalMove
                except IndexError:
                    continue
            for z in horse_moves:
                try:
                    if board[b + z] == ['BH']:
                        try:
                            if XiangqiGame.horse_move(self, loc=b + z, dest=b):
                                raise GeneralCheck
                        except NotALegalMove:
                            continue
                        except GeneralCheck:
                            raise NotALegalMove
                except IndexError:
                    continue
            for z in general_moves:
                try:
                    if board[b + z] == ['BG']:
                        if loop_counter == 0:
                            try:
                                if XiangqiGame.general_move(self, 1, loc=b+z, dest=b):
                                    raise GeneralCheck
                                else:
                                    continue
                            except NotALegalMove:
                                continue
                            except GeneralCheck:
                                raise NotALegalMove
                except IndexError:
                    continue
        if move_counter % 2 != 0:
            b = destination
            for z in soldier_moves:
                try:
                    if board[b + z] == ['RS']:
                        try:
                            if XiangqiGame.soldier_move(self, loc=b + z, dest=b):
                                raise GeneralCheck
                        except NotALegalMove:
                            continue
                        except GeneralCheck:
                            raise NotALegalMove
                except IndexError:
                    continue
            for z in cannon_moves:
                try:
                    if board[b + z] == ['RN']:
                        try:
                            if XiangqiGame.cannon_move(self, 1, loc=b + z, dest=b):
                                raise GeneralCheck
                        except NotALegalMove:
                            continue
                        except GeneralCheck:
                            raise NotALegalMove
                except IndexError:
                    continue
                try:
                    if board[b + z] == ['RC']:
                        try:
                            if XiangqiGame.chariot_move(self, loc=b + z, dest=b):
                                raise GeneralCheck
                        except NotALegalMove:
                            continue
                        except GeneralCheck:
                            raise NotALegalMove
                except IndexError:
                    continue
            for z in horse_moves:
                try:
                    if board[b + z] == ['RH']:
                        try:
                            if XiangqiGame.horse_move(self, loc=b + z, dest=b):
                                raise GeneralCheck
                        except NotALegalMove:
                            continue
                        except GeneralCheck:
                            raise NotALegalMove
                except IndexError:
                    continue
            for z in general_moves:
                try:
                    if board[b + z] == ['RG']:
                        if loop_counter == 0:
                            try:
                                if XiangqiGame.general_move(self, 1, loc=b+z, dest=b):
                                    raise GeneralCheck
                                else:
                                    continue
                            except NotALegalMove:
                                continue
                            except GeneralCheck:
                                raise NotALegalMove
                except IndexError:
                    continue
        # If all the tests pass, return True
        return True

    # Create a function that returns the game state
    def get_game_state(self):
        # return the game state data member
        return self.__game_state

    # Create a function to check if the general of the color passed as an argument is in check
    def is_in_check(self, color):
        # Create a variable to hold the color and the two viable colors for comparison
        b_check = 'black'
        r_check = 'red'
        c_check = color
        # compare the string that was entered to the two viable colors.  If it matches one of them, return False if that
        # color is not in check and True if it is in check
        if c_check.casefold() == b_check.casefold():
            b_test = self.__black_check
            if b_test == 'NOT IN CHECK':
                return False
            else:
                return True

        if c_check.casefold() == r_check.casefold():
            r_test = self.__red_check
            if r_test == 'NOT IN CHECK':
                return False
            else:
                return True
        # Return False if the color was not one of the two viable colors
        return False

    # Create a function to make a move.  It takes a string of the spot you are moving from and the spot you are moving
    # To and will call the correct piece function for the piece in the current spot
    def make_move(self, left, to):
        # Create variables for a column counter, a row counter, the game state, viable piece movements, and the board
        game_state = self.__game_state
        count_col = 0
        count_row = 0
        board = self.__board
        move_counter = self.__move_counter
        red_soldier_moves = [1, 10, -10]
        black_soldier_moves = [-1, 10, -10]
        general_moves = [1, -1, 10, -10, 70, -70, 80, -80, 90, -90]
        cannon_moves = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 1, -1, 2, -2,
                        3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]
        horse_moves = [8, -8, 12, -12, 19, -19, 21, -21]
        elephant_moves = [18, -18, 22, -22]
        advisor_moves = [9, -9, 11, -11]
        # If the game has a winner, return False
        if game_state != 'UNFINISHED':
            return False
        # Split the string of the board spot you are moving from and take
        # The column letter and the row number to variables
        moved_from = [[char] for char in left]
        moved_from_col = moved_from[0]
        moved_from_row = moved_from[1]
        # Split the string of the board spot you are moving to and take
        # The column letter and the row number to variables
        moved_to = [[char] for char in to]
        moved_to_col = moved_to[0]
        moved_to_row = moved_to[1]

        # Check to see if the string for the spot you are moving from/to is 3 characters long.  If so, you must be
        # Dealing with row number 10.  Combine the 1 and 0 string to remake that number.
        if len(moved_from) == 3:
            test_str = []
            test_str.append(moved_from[1][0])
            test_str.append(moved_from[2][0])
            test_3 = ''.join(test_str[0:2])
            moved_from_row = [str(test_3)]
        if len(moved_to) == 3:
            test_str = []
            test_str.append(moved_to[1][0])
            test_str.append(moved_to[2][0])
            test_3 = ''.join(test_str[0:2])
            moved_to_row = [str(test_3)]

        # Count through the board list, comparing the first character in each sublist with the letter of the space you
        # Are moving from, adding 1 for every space that isn't the one you are looking for. When you find the target
        # Sub-list, move on to the next for loop
        for i, e in enumerate(board):
            lett = [char for char in board[i][0]]
            lett_check = [lett[0]]
            if lett_check != moved_from_col:
                count_col += 1
            else:
                break
        # Count through the board list, comparing the each sublist with the number of the space you
        # Are moving from, adding 1 for every space that isn't the one you are looking for. When you find the target
        # Sub-list, add the counter for row and column together into a variable and reset the counters.
        for o, p in enumerate(board):
            if p != moved_from_row:
                count_row += 1
            else:
                spot_from = count_col + count_row
                count_col = 0
                count_row = 0
                break
        # Check to see if the spot you are trying to move from is empty.  If so, raise an error.  If not,
        # Split the string of the piece and put that into a variable as a list.  Create a variable to hold the second
        # Letter of the piece.
        if board[spot_from] == ['  ']:
            return
        else:
            piece = [char for char in board[spot_from][0]]
            piece_check = piece[1]
        lett = [char for char in board[spot_from][0]]
        # Check to see if it is not the turn of the piece that is trying to move.  If so, return False
        if lett[0] == 'R':
            if move_counter % 2 != 0:
                return False
        if lett[0] == 'B':
            if move_counter % 2 == 0:
                return False
        # Count through the board list, comparing the first character in each sublist with the letter of the space you
        # Are moving to, adding 1 for every space that isn't the one you are looking for. When you find the target
        # Sub-list, move on to the next for loop
        for u, z in enumerate(board):
            lett = [char for char in board[u][0]]
            lett_check = [lett[0]]
            if lett_check != moved_to_col:
                count_col += 1
            else:
                break
        # Count through the board list, comparing the each sublist with the number of the space you
        # Are moving to, adding 1 for every space that isn't the one you are looking for. When you find the target
        # Sub-list, add the counter for row and column together into a variable and reset the counters.
        for l, b in enumerate(board):
            if b != moved_to_row:
                count_row += 1
            else:
                spot_to = count_col + count_row
                break
        # Take the variable that holds the second letter of the piece and run the function for movement that is relevant
        # To that piece.  If the move is not viable, return False
        if piece_check == 'E':
            try:
                XiangqiGame.elephant_move(self, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        if piece_check == 'G':
            try:
                XiangqiGame.general_move(self, 0, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        if piece_check == 'A':
            try:
                XiangqiGame.advisor_move(self, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        if piece_check == 'H':
            try:
                XiangqiGame.horse_move(self, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        if piece_check == 'C':
            try:
                XiangqiGame.chariot_move(self, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        if piece_check == 'N':
            try:
                XiangqiGame.cannon_move(self, 0, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        if piece_check == 'S':
            try:
                XiangqiGame.soldier_move(self, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        # Place the string in the current sublist location and cast it into a variable.  Replace that location with a 
        # Blank board string, and move the piece to the destination
        piece = board[spot_from]
        board[spot_from] = ['  ']
        board[spot_to] = piece
        # Increase the move counter by 1 and run the check_check function to see if anyone is currently in check
        move_counter += 1
        self.__move_counter = move_counter
        XiangqiGame.check_check(self, board=board)
        # If the move that was just made causes their own team to be in check, reverse the move and return False.  Else,
        # Run the viable_moves function to see if the opponent has any viable moves left.  If so, return True, if not,
        # Change the game status to the winner and return True.
        if move_counter % 2 != 0:
            if XiangqiGame.is_in_check(self, 'red'):
                board[spot_from] = piece
                board[spot_to] = ['  ']
                move_counter -= 1
                self.__move_counter = move_counter
                return False
            for v in range(0, 110):
                try:
                    if board[v] == ['BG']:
                        for x in general_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                    if board[v] == ['BS']:
                        for x in black_soldier_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                    if board[v] == ['BA']:
                        for x in advisor_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                    if board[v] == ['BC']:
                        for x in cannon_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                    if board[v] == ['BN']:
                        for x in cannon_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                    if board[v] == ['BE']:
                        for x in elephant_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                    if board[v] == ['BH']:
                        for x in horse_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                except NotALegalMove:
                    continue
                except IndexError:
                    continue
            game_state = 'RED_WON'
            self.__game_state = game_state
            return True
        if move_counter % 2 == 0:
            if XiangqiGame.is_in_check(self, 'black'):
                board[spot_from] = piece
                board[spot_to] = ['  ']
                move_counter -= 1
                self.__move_counter = move_counter
                return False
            for v in range(0, 110):
                try:
                    if board[v] == ['RG']:
                        for x in general_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                    if board[v] == ['RS']:
                        for x in red_soldier_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                    if board[v] == ['RA']:
                        for x in advisor_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                    if board[v] == ['RC']:
                        for x in cannon_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                    if board[v] == ['RN']:
                        for x in cannon_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                    if board[v] == ['RE']:
                        for x in elephant_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                    if board[v] == ['RH']:
                        for x in horse_moves:
                            try:
                                if XiangqiGame.viable_move(self, left=v, to=v+x):
                                    return True
                            except NotALegalMove:
                                continue
                            except IndexError:
                                continue
                except NotALegalMove:
                    continue
                except IndexError:
                    continue
            game_state = 'BLACK_WON'
            self.__game_state = game_state
            return True

    # A function that tells whether anyone is currently in check or not.
    def check_check(self, board):
        # Initialize the current check status of both players, the value passed as the board, the move counter, the
        # Viable moves for all pieces, and the numbers along the left hand side of the board
        black_check = self.__black_check
        red_check = self.__red_check
        board = board
        move_counter = self.__move_counter - 1
        soldier_moves = [1, -1, 10, -10]
        black_general_moves = [1, -1, 10, -10, 70, 80, 90]
        red_general_moves = [1, -1, 10, -10, -70, -80, -90]
        cannon_moves = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80,
                        90, -90, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]
        horse_moves = [8, -8, 12, -12, 19, -19, 21, -21]
        end_check = ['1','2','3','4','5','6','7','8','9','10']
        # Find the black general in the board
        for o in range(0, 110):
                if board[o] == ['BG']:
                    # Check to see if the red general is across the board from the black general.  If so, check to see
                    # If any pieces are between them.  If there are, raise the NotCheck error.  If there aren't,
                    # set the black check status to IS IN CHECK
                    for p in black_general_moves:
                        try:
                            if board[o + p] == ['RG']:
                                str_int = [char for char in str(p)]
                                check_test = 0
                                if str_int[0] == '-':
                                    for t in range(1, int(str_int[1])):
                                        y = t * 10
                                        if board[o + y] != ['  ']:
                                            check_test += 1
                                    if check_test > 0:
                                        raise NotCheck
                                    if black_check == 'NOT IN CHECK':
                                        black_check = 'IN CHECK'
                                        self.__black_check = black_check
                                        return
                                    if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                        return
                                else:
                                    for t in range(1, int(str_int[0])):
                                        y = t * 10
                                        if board[o + y] != ['  ']:
                                            check_test += 1
                                    if check_test > 0:
                                        raise NotCheck
                                    if black_check == 'NOT IN CHECK':
                                        black_check = 'IN CHECK'
                                        self.__black_check = black_check
                                        return
                                    if black_check != 'NOT IN CHECK':
                                        return
                        except IndexError:
                            continue
                        except NotCheck:
                            continue
                    # Check to see if red soldiers are in range of the black general. If there aren't, raise the
                    # NotCheck error.  If there are, set the black check status to IS IN CHECK
                    for p in soldier_moves:
                        try:
                            if board[o + p] == ['RS']:
                                if black_check == 'NOT IN CHECK':
                                    black_check = 'IN CHECK'
                                    self.__black_check = black_check
                                    return
                            if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                return
                        except:
                            continue
                    # Check to see if red horses are in legal range of the black general. If there aren't, raise the
                    # NotCheck error.  If there are, set the black check status to IS IN CHECK
                    for p in horse_moves:
                        try:
                            if board[o + p] == ['RH']:
                                if p == -8:
                                    if board[o - 9] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if black_check == 'NOT IN CHECK':
                                            black_check = 'IN CHECK'
                                            self.__black_check = black_check
                                            return
                                        if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                            return
                                if p == 8:
                                    if board[o + 9] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if black_check == 'NOT IN CHECK':
                                            black_check = 'IN CHECK'
                                            self.__black_check = black_check
                                            return
                                        if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                            return
                                if p == -12:
                                    if board[o - 11] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if black_check == 'NOT IN CHECK':
                                            black_check = 'IN CHECK'
                                            self.__black_check = black_check
                                            return
                                        if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                            return
                                if p == 12:
                                    if board[o + 11] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if black_check == 'NOT IN CHECK':
                                            black_check = 'IN CHECK'
                                            self.__black_check = black_check
                                            return
                                        if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                            return
                                if p == -19:
                                    if board[o - 9] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if black_check == 'NOT IN CHECK':
                                            black_check = 'IN CHECK'
                                            self.__black_check = black_check
                                            return
                                        if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                            return
                                if p == 19:
                                    if board[o + 9] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if black_check == 'NOT IN CHECK':
                                            black_check = 'IN CHECK'
                                            self.__black_check = black_check
                                            return
                                        if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                            return
                                if p == -21:
                                    if board[o - 11] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if black_check == 'NOT IN CHECK':
                                            black_check = 'IN CHECK'
                                            self.__black_check = black_check
                                            return
                                        if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                            return
                                if p == 21:
                                    if board[o + 11] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if black_check == 'NOT IN CHECK':
                                            black_check = 'IN CHECK'
                                            self.__black_check = black_check
                                            return
                                        if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                            return
                        except IndexError:
                            continue
                        except NotCheck:
                            continue
                    # Check to see if red cannons or chariots are in legal range of the black general.
                    # If there aren't, raise the NotCheck error.  If there are,set the black check status to IS IN CHECK
                    for p in cannon_moves:
                        try:
                            if board[o + p] == ['RC']:
                                str_int = [char for char in str(p)]
                                check_test = 0
                                if len(str_int) == 3:
                                    for t in range(1, int(str_int[1])):
                                        y = t * -10
                                        if board[o + y] != ['  ']:
                                            check_test += 1
                                    if check_test > 0:
                                        raise NotCheck
                                    if black_check == 'NOT IN CHECK':
                                        black_check = 'IN CHECK'
                                        self.__black_check = black_check
                                        return
                                    if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                        return
                                if len(str_int) == 2:
                                    if str_int[0] == '-':
                                        for t in range(1, int(str_int[1])):
                                            y = t * -1
                                            if board[o + y] != ['  ']:
                                                check_test += 1
                                        if check_test > 0:
                                            raise NotCheck
                                        if black_check == 'NOT IN CHECK':
                                            black_check = 'IN CHECK'
                                            self.__black_check = black_check
                                            return
                                        if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                            return
                                    else:
                                        for t in range(1, int(str_int[0])):
                                            y = t * 10
                                            if board[o + y] != ['  ']:
                                                check_test += 1
                                        if check_test > 0:
                                            raise NotCheck
                                        if black_check == 'NOT IN CHECK':
                                            black_check = 'IN CHECK'
                                            self.__black_check = black_check
                                            return
                                        if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                            return
                                if len(str_int) == 1:
                                    for t in range(1, int(str_int[0])):
                                        if board[o + t] != ['  ']:
                                            check_test += 1
                                    if check_test > 0:
                                        raise NotCheck
                                    if black_check == 'NOT IN CHECK':
                                        black_check = 'IN CHECK'
                                        self.__black_check = black_check
                                        return
                                    if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                        return
                        except NotCheck:
                            continue
                        except IndexError:
                            continue
                        try:
                            if board[o + p] == ["RN"]:
                                if p == 1 or p == -1 or p == 10 or p == -10:
                                    raise NotCheck
                                str_int = [char for char in str(p)]
                                check_test = 0
                                if len(str_int) == 3:
                                    for t in range(1, int(str_int[1])):
                                        y = t * -10
                                        if board[o + y] != ['  ']:
                                            check_test += 1
                                    if check_test != 1:
                                        raise NotCheck
                                    if black_check == 'NOT IN CHECK':
                                        black_check = 'IN CHECK'
                                        self.__black_check = black_check
                                        return
                                    if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                        return
                                if len(str_int) == 2:
                                    if str_int[0] == '-':
                                        for t in range(1, int(str_int[1])):
                                            y = t * -1
                                            if board[o + y] != ['  ']:
                                                if board[o + y][0] in end_check:
                                                    continue
                                                check_test += 1
                                        if check_test != 1:
                                            raise NotCheck
                                        if black_check == 'NOT IN CHECK':
                                            black_check = 'IN CHECK'
                                            self.__black_check = black_check
                                            return
                                        if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                            return
                                    else:
                                        for t in range(1, int(str_int[0])):
                                            y = t * 10
                                            if board[o + y] != ['  ']:
                                                check_test += 1
                                        if check_test != 1:
                                            raise NotCheck
                                        if black_check == 'NOT IN CHECK':
                                            black_check = 'IN CHECK'
                                            self.__black_check = black_check
                                            return
                                        if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                            return
                                if len(str_int) == 1:
                                    for t in range(1, int(str_int[0])):
                                        if board[o + t] != ['  ']:
                                            if board[o + t][0] in end_check:
                                                continue
                                            check_test += 1
                                    if check_test != 1:
                                        raise NotCheck
                                    if black_check == 'NOT IN CHECK':
                                        black_check = 'IN CHECK'
                                        self.__black_check = black_check
                                        return
                                    if black_check != 'NOT IN CHECK' and move_counter % 2 == 0:
                                        return
                        except NotCheck:
                            continue
                        except IndexError:
                            continue
                    # If all tests pass, the black general status is set to NOT IN CHECK
                    black_check = 'NOT IN CHECK'
                    self.__black_check = black_check
        # Find the red general in the board
        for o in range(0, 110):
                if board[o] == ['RG']:
                    # Check to see if the black general is across the board from the red general.  If so, check to see
                    # If any pieces are between them.  If there are, raise the NotCheck error.  If there aren't,
                    # set the red check status to IS IN CHECK
                    for p in red_general_moves:
                        try:
                            if board[o + p] == ['BG']:
                                str_int = [char for char in str(p)]
                                check_test = 0
                                for t in range(1, int(str_int[1])):
                                    y = t * -10
                                    if board[o + y] != ['  ']:
                                        check_test += 1
                                if check_test > 0:
                                    raise NotCheck
                                if red_check == 'NOT IN CHECK':
                                    red_check = 'IN CHECK'
                                    self.__red_check = red_check
                                    return
                                if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                    return
                        except IndexError:
                            continue
                        except NotCheck:
                            continue
                    # Check to see if black soldiers are in range of the black general. If there aren't, raise the
                    # NotCheck error.  If there are, set the red check status to IS IN CHECK
                    for p in soldier_moves:
                        try:
                            if board[o + p] == ['BS']:
                                if red_check == 'NOT IN CHECK':
                                    red_check = 'IN CHECK'
                                    self.__red_check = red_check
                                    return
                                if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                    return
                        except:
                            continue
                    # Check to see if black horses are in legal range of the black general. If there aren't, raise the
                    # NotCheck error.  If there are, set the red check status to IS IN CHECK
                    for p in horse_moves:
                        try:
                            if board[o + p] == ['BH']:
                                if p == -8:
                                    if board[o - 9] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if red_check == 'NOT IN CHECK':
                                            red_check = 'IN CHECK'
                                            self.__red_check = red_check
                                            return
                                        if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                            return
                                if p == 8:
                                    if board[o + 9] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if red_check == 'NOT IN CHECK':
                                            red_check = 'IN CHECK'
                                            self.__red_check = red_check
                                            return
                                        if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                            return
                                if p == -12:
                                    if board[o - 11] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if red_check == 'NOT IN CHECK':
                                            red_check = 'IN CHECK'
                                            self.__red_check = red_check
                                            return
                                        if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                            return
                                if p == 12:
                                    if board[o + 11] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if red_check == 'NOT IN CHECK':
                                            red_check = 'IN CHECK'
                                            self.__red_check = red_check
                                            return
                                        if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                            return
                                if p == -19:
                                    if board[o - 9] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if red_check == 'NOT IN CHECK':
                                            red_check = 'IN CHECK'
                                            self.__red_check = red_check
                                            return
                                        if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                            return
                                if p == 19:
                                    if board[o + 9] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if red_check == 'NOT IN CHECK':
                                            red_check = 'IN CHECK'
                                            self.__red_check = red_check
                                            return
                                        if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                            return
                                if p == -21:
                                    if board[o - 11] != ['  ']:
                                        pass
                                    else:
                                        if red_check == 'NOT IN CHECK':
                                            red_check = 'IN CHECK'
                                            self.__red_check = red_check
                                            return
                                        if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                            return
                                if p == 21:
                                    if board[o + 11] != ['  ']:
                                        raise NotCheck
                                    else:
                                        if red_check == 'NOT IN CHECK':
                                            red_check = 'IN CHECK'
                                            self.__red_check = red_check
                                            return
                                        if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                            return
                        except IndexError:
                            continue
                        except NotCheck:
                            continue
                    # Check to see if black cannons or chariots are in legal range of the black general.
                    # If there aren't, raise the NotCheck error.  If there are,set the red check status to IS IN CHECK
                    for p in cannon_moves:
                        try:
                            if board[o + p] == ['BC']:
                                str_int = [char for char in str(p)]
                                check_test = 0
                                if len(str_int) == 3:
                                    for t in range(1, int(str_int[1])):
                                        y = t * -10
                                        if board[o + y] != ['  ']:
                                            check_test += 1
                                    if check_test > 0:
                                        raise NotCheck
                                    if red_check == 'NOT IN CHECK':
                                        red_check = 'IN CHECK'
                                        self.__red_check = red_check
                                        return
                                    if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                        return
                                if len(str_int) == 2:
                                    if str_int[0] == '-':
                                        for t in range(1, int(str_int[1])):
                                            y = t * -1
                                            if board[o + y] != ['  ']:
                                                check_test += 1
                                        if check_test > 0:
                                            raise NotCheck
                                        if red_check == 'NOT IN CHECK':
                                            red_check = 'IN CHECK'
                                            self.__red_check = red_check
                                            return
                                        if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                            return
                                    else:
                                        if str_int[0] == '1':
                                                red_check = 'IN CHECK'
                                                self.__red_check = red_check
                                                return
                                        for t in range(1, int(str_int[0])):
                                            y = t * 10
                                            if board[o + y] != ['  ']:
                                                check_test += 1
                                        if check_test > 0:
                                            raise NotCheck
                                        if red_check == 'NOT IN CHECK':
                                            red_check = 'IN CHECK'
                                            self.__red_check = red_check
                                            return
                                        if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                            return
                                if len(str_int) == 1:
                                        for t in range(1, int(str_int[0])):
                                            if board[o + t] != ['  ']:
                                                check_test += 1
                                        if check_test > 0:
                                            raise NotCheck
                                        if red_check == 'NOT IN CHECK':
                                            red_check = 'IN CHECK'
                                            self.__red_check = red_check
                                            return
                                        if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                            return
                        except NotCheck:
                            continue
                        except IndexError:
                            continue
                        try:
                            if board[o + p] == ["BN"]:
                                if p == 1 or p == -1 or p == 10 or p == -10:
                                    raise NotCheck
                                str_int = [char for char in str(p)]
                                check_test = 0
                                if len(str_int) == 3:
                                    for t in range(1, int(str_int[1])):
                                        y = t * -10
                                        if board[o + y] != ['  ']:
                                            check_test += 1
                                    if check_test != 1:
                                        raise NotCheck
                                    if red_check == 'NOT IN CHECK':
                                        red_check = 'IN CHECK'
                                        self.__red_check = red_check
                                        return
                                    if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                        return
                                if len(str_int) == 2:
                                    if str_int[0] == '-':
                                        for t in range(1, int(str_int[1])):
                                            y = t * -1
                                            if board[o + y] != ['  ']:
                                                if board[o + y][0] in end_check:
                                                    continue
                                                check_test += 1
                                        if check_test != 1:
                                            raise NotCheck
                                        if red_check == 'NOT IN CHECK':
                                            red_check = 'IN CHECK'
                                            self.__red_check = red_check
                                            return
                                        if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                            return
                                    else:
                                        for t in range(1, int(str_int[0])):
                                            y = t * 10
                                            if board[o + y] != ['  ']:
                                                check_test += 1
                                        if check_test != 1:
                                            raise NotCheck
                                        if red_check == 'NOT IN CHECK':
                                            red_check = 'IN CHECK'
                                            self.__red_check = red_check
                                            return
                                        if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                            return
                                if len(str_int) == 1:
                                    for t in range(1, int(str_int[0])):
                                        if board[o + t] != ['  ']:
                                            if board[o + t][0] in end_check:
                                                continue
                                            check_test += 1
                                    if check_test != 1:
                                        raise NotCheck
                                    if red_check == 'NOT IN CHECK':
                                        red_check = 'IN CHECK'
                                        self.__red_check = red_check
                                        return
                                    if red_check != 'NOT IN CHECK' and move_counter % 2 != 0:
                                        return
                        except NotCheck:
                            continue
                        except IndexError:
                            continue
                    # If all tests pass, the red general status is set to NOT IN CHECK
                    red_check = 'NOT IN CHECK'
                    self.__red_check = red_check
        return

    # a function that is passed locations and sees if they are viable
    def viable_move(self, left, to):
        # Initialize variables for a copy of the board for testing, the state of the game, a move counter, the current
        # Location and the destination location
        board = self.__board[:]
        game_state = self.__game_state
        move_counter = self.__move_counter
        spot_from = left
        spot_to = to
        # If the game has a winner, return False
        if game_state != 'UNFINISHED':
            return False

        # Check to see if the spot you are trying to move from is empty.  If so, return False.  If not,
        # Split the string of the piece and put that into a variable as a list.  Create a variable to hold the second
        # Letter of the piece.
        if board[spot_from] == ['  ']:
            return False
        else:
            piece = [char for char in board[spot_from][0]]
            piece_check = piece[1]
        lett = [char for char in board[spot_from][0]]

        # If it is not the turn of the opposing player to the piece that is trying to move, return False
        if lett[0] == 'R':
            if move_counter % 2 != 0:
                return False
        if lett[0] == 'B':
            if move_counter % 2 == 0:
                return False
        # Take the second letter of the piece and run the relevant movement function to it.  If it returns true,
        # Continue.  If it is not a viable move, return False.
        if piece_check == 'E':
            try:
                XiangqiGame.elephant_move(self, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        if piece_check == 'G':
            try:
                XiangqiGame.general_move(self, 0, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        if piece_check == 'A':
            try:
                XiangqiGame.advisor_move(self, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        if piece_check == 'H':
            try:
                XiangqiGame.horse_move(self, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        if piece_check == 'C':
            try:
                XiangqiGame.chariot_move(self, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        if piece_check == 'N':
            try:
                XiangqiGame.cannon_move(self, 0, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        if piece_check == 'S':
            try:
                XiangqiGame.soldier_move(self, loc=spot_from, dest=spot_to)
            except NotALegalMove:
                return False
        # Take the piece from the spot it currently is, cast it into a variable, put a blank board string in its place,
        # And move it to the destination.
        piece = board[spot_from]
        board[spot_from] = ['  ']
        board[spot_to] = piece
        # Check to see if the player on the test board is still in check
        XiangqiGame.check_check(self, board=board)
        # If the player you are testing for is still in check, return False.
        if move_counter % 2 == 0:
            if XiangqiGame.is_in_check(self, 'red'):
                board[spot_from] = piece
                board[spot_to] = ['  ']
                return False
        if move_counter % 2 != 0:
            if XiangqiGame.is_in_check(self, 'black'):
                board[spot_from] = piece
                board[spot_to] = ['  ']
                return False
        return True


# A custom error that is raised if the piece is not in check
class NotCheck(Exception):
    pass


# A custom error that is raised if the move is not legal
class NotALegalMove(Exception):
    pass


# A custom error that is raised if the move puts the general in check
class GeneralCheck(Exception):
    pass
