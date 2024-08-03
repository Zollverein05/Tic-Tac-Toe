board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")

def make_move(player):
    while (True):
        position = int(input(f"Player {player}, enter position (1-9): ")) - 1
        if (0 <= position <= 8 and board[position] == " "):
            board[position] = player
            break
        else:
            print("Invalid move. Try again.")

def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def play_game():
    for turn in range(9):
        player = "X" if turn % 2 == 0 else "O"
        print_board()
        make_move(player)
        if check_win(player):
            print_board()
            print(f"Player {player} wins!")
            return
    print_board()
    print("It's a tie!")

play_game()