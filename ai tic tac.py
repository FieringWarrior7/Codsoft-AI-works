import math
# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a winner
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    # Check for a tie
    if all(board[row][col] != ' ' for row in range(3) for col in range(3)):
        return 'Tie'
    
    return None

# Minimax algorithm implementation
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    
    if winner == 'X':  # AI wins
        return 1
    if winner == 'O':  # Human wins
        return -1
    if winner == 'Tie':  # Tie
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score

# Function to find the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                score = minimax(board, 0, False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe!")
    
    while True:
        # Human player's turn (O)
        print_board(board)
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Spot already taken!")
            continue
        
        if check_winner(board) is not None:
            break
        
        # AI's turn (X)
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'X'
        
        if check_winner(board) is not None:
            break
    
    print_board(board)
    winner = check_winner(board)
    if winner == 'Tie':
        print("It's a tie!")
    else:
        print(f"The winner is {winner}!")

# Start the game
play_game()

