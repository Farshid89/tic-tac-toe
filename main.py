WIN_CONDITIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

board_map = {1: "   ", 2: "   ", 3: "   ", 4: "   ", 5: "   ", 6: "   ", 7: "   ", 8: "   ", 9: "   "}
available_cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1_cells = []
player2_cells = []
game_is_on = True


# Print Board
def board():
    line1 = board_map[1] + "|" + board_map[2] + "|" + board_map[3]
    line2 = board_map[4] + "|" + board_map[5] + "|" + board_map[6]
    line3 = board_map[7] + "|" + board_map[8] + "|" + board_map[9]
    result = f"{line1}\n------------\n{line2}\n------------\n{line3}"
    return result


def check_winner(cells):
    is_winner = False
    for win in WIN_CONDITIONS:
        is_winner = all(item in cells for item in win)
        if is_winner:
            break
    return is_winner


def is_cell_available(number):
    if number in available_cells:
        return True
    return False


def get_user_input(player):
    choice = ""
    is_valid = True
    try:
        choice = int(input(f"{player} please choose a cell: "))
    except ValueError:
        is_valid = False
    # Check if cell is available
    while not is_cell_available(choice):
        if not is_valid:
            print("Please enter an integer number between 1-9.")
        else:
            print("The chosen cell is not available! Try again.")
        is_valid = True
        try:
            choice = int(input(f"{player} please choose a cell: "))
        except ValueError:
            is_valid = False
    return choice


print("Welcome to Tic-Tac_Toe Game")
player1_name = input("Please enter first player name: ")
player2_name = input("Please enter second player name: ")
print(board())
while game_is_on and len(available_cells) > 0:
    player1_choice = get_user_input(player1_name)
    available_cells.remove(player1_choice)
    player1_cells.append(player1_choice)
    board_map[player1_choice] = " O "
    print(board())

# Check in Player 1 wins
    if check_winner(player1_cells):
        print(f"{player1_name} Won!")
        game_is_on = False
        print(f"{player1_name}'s Cells: {player1_cells}")
        break
    print(f"{player1_name}'s Cells: {player1_cells}")
    if len(available_cells) < 1:
        break

    player2_choice = get_user_input(player2_name)
    available_cells.remove(player2_choice)
    player2_cells.append(player2_choice)
    board_map[player2_choice] = " X "
    print(board())

    # Check in Player 2 wins
    if check_winner(player2_cells):
        print(f"{player2_name} Won!")
        game_is_on = False
        print(f"{player2_name}'s Cells: {player2_cells}")
        break
    print(f"{player2_name}'s Cells: {player2_cells}")

if len(available_cells) < 1:
    print("DRAW!")
