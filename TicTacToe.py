#Tic Tac Toe using python
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print("-"*9)
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
def tic_tac_toe():
    board = [[' ' for i in range(3)] for _ in range(3)]
    player = 'x'
    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, 2): "))
        
        if board[row][col] != ' ':
            print("This position is already taken. Try again.")
            continue
        board[row][col] = player
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if all(all(cell != ' ' for cell in row) for row in board):
            print_board(board)
            print("it's a tie!")
        
        player = 'o' if player == 'x' else 'x'

tic_tac_toe()