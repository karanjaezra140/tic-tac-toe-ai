import random

def create_board():
    """
    Creates a new empty Tic-Tac-Toe board.
    The board is a list of 9 elements (index 0-8), representing:
    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8
    Each cell starts as a space " " (empty).
    """
    return [" " for _ in range(9)]  # 9 empty cells


def print_board(board):
    """
    Prints the current state of the board in a readable 3x3 grid format.
    """
    print()  # blank line for spacing
    for row in range(3):  # loop over the 3 rows
        # get the 3 cells belonging to this row
        cells = board[row * 3: row * 3 + 3]
        print(" " + " | ".join(cells))  # print cells separated by |
        if row < 2:  # don't print a divider after the last row
            print("---+---+---")
    print()


def is_valid_move(board, position):
    """
    Checks if a move is valid.
    A move is valid if the position is between 0-8 AND the cell is empty.
    """
    if position < 0 or position > 8:  # out of range check
        return False
    if board[position] != " ":  # cell already taken
        return False
    return True


def get_player_move(board):
    """
    Asks the human player for a move and validates it.
    Keeps asking until a valid move is entered.
    Returns the chosen position (0-8) as an integer.
    """
    while True:  # loop until valid input is given
        move = input("Enter your move (0-8): ")

        if not move.isdigit():  # reject non-numeric input
            print("Please enter a number between 0 and 8.")
            continue

        move = int(move)  # convert to integer now that we know it's a digit

        if is_valid_move(board, move):
            return move  # valid move found, exit loop and return it
        else:
            print("That move is invalid or already taken. Try again.")


def make_move(board, position, player):
    """
    Places a player's symbol ('X' or 'O') on the board at the given position.
    Assumes the move has already been validated.
    """
    board[position] = player
    return board

def check_winner(board, player):
    """
    Checks if the given player ('X' or 'O') has won.
    Checks all 8 possible winning combinations:
    3 rows, 3 columns, 2 diagonals.
    Returns True if that player has won, False otherwise.
    """
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    for combo in winning_combinations:  # check each combination
        a, b, c = combo
        if board[a] == board[b] == board[c] == player:
            return True  # all 3 cells match the player's symbol

    return False  # no winning combination found


def is_board_full(board):
    """
    Checks if the board has no empty cells left (used to detect a draw).
    """
    return " " not in board  # True if there are no empty spaces left


def check_game_over(board):
    """
    Checks the overall game state after a move.
    Returns one of: "X_WINS", "O_WINS", "DRAW", or "CONTINUE".
    """
    if check_winner(board, "X"):
        return "X_WINS"
    elif check_winner(board, "O"):
        return "O_WINS"
    elif is_board_full(board):
        return "DRAW"
    else:
        return "CONTINUE"  # game isn't over yet


def minimax(board, depth, is_maximizing):
    """
    Recursive Minimax algorithm.
    'is_maximizing' = True means it's the AI's (O's) turn to maximize its score.
    'is_maximizing' = False means it's the human's (X's) turn, who minimizes AI's score.
    Returns a score: +10 for AI win, -10 for human win, 0 for draw.
    Depth is subtracted/added so the AI prefers to win FASTER and lose SLOWER.
    """
    result = check_game_over(board)

    # base cases: someone won or it's a draw, so stop recursing
    if result == "O_WINS":
        return 10 - depth
    elif result == "X_WINS":
        return depth - 10
    elif result == "DRAW":
        return 0

    if is_maximizing:  # AI's turn (O) - trying to get the highest score
        best_score = -1000
        for i in range(9):
            if board[i] == " ":  # try every empty cell
                board[i] = "O"                              # make the move
                score = minimax(board, depth + 1, False)     # simulate human's response
                board[i] = " "                                # undo the move (backtrack)
                best_score = max(best_score, score)          # keep the best outcome
        return best_score
    else:  # Human's turn (X) - trying to get the lowest score (worst for AI)
        best_score = 1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score


def get_ai_move(board):
    """
    Determines the AI's best move using Minimax.
    Loops through all empty cells, simulates each one, and picks
    whichever move gives the AI the highest possible score.
    """
    best_score = -1000
    best_move = None

    for i in range(9):
        if board[i] == " ":               # only consider empty cells
            board[i] = "O"                  # try this move as the AI
            score = minimax(board, 0, False) # score it assuming human plays next
            board[i] = " "                   # undo the move

            if score > best_score:          # keep track of the best one found
                best_score = score
                best_move = i

    return best_move


def play_game():
    """
    Runs a full game of Tic-Tac-Toe: human (X) vs AI (O).
    The starting player is chosen randomly each game.
    Handles turn order, checks for game-over conditions after every move,
    and announces the result at the end.
    """
    board = create_board()
    print("Welcome to Tic-Tac-Toe! You are X, the AI is O.")

    # randomly decide who starts: "X" (human) or "O" (AI)
    current_player = random.choice(["X", "O"])
    if current_player == "X":
        print("You go first!")
    else:
        print("The AI goes first this round!")

    print_board(board)

    while True:  # keep looping until the game ends
        if current_player == "X":
            move = get_player_move(board)       # ask the human for a move
            board = make_move(board, move, "X")
        else:
            print("AI is thinking...")
            move = get_ai_move(board)           # let the AI decide
            board = make_move(board, move, "O")
            print(f"AI played position {move}.")

        print_board(board)

        status = check_game_over(board)  # check result after this move

        if status == "X_WINS":
            print("Congratulations, you win!")
            break
        elif status == "O_WINS":
            print("The AI wins. Better luck next time!")
            break
        elif status == "DRAW":
            print("It's a draw!")
            break

        # switch turns
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()