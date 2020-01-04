import os
import time

# clear a terminal
def clear():
    os.system("cls")


# create a board each segment has a placeholder to choose later in the game where to put a symbol
def show_board(board):
    clear()
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("-----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")


def check_win(board, symbol):
    if symbol != "" and (
        (board[1] == board[2] == board[3] == symbol)
        or (board[4] == board[5] == board[6] == symbol)
        or (board[7] == board[8] == board[9] == symbol)
        or (board[1] == board[4] == board[7] == symbol)
        or (board[2] == board[5] == board[8] == symbol)
        or (board[3] == board[6] == board[9] == symbol)
        or (board[1] == board[5] == board[9] == symbol)
        or (board[3] == board[5] == board[7] == symbol)
    ):

        return True

    elif " " not in board:
        print("Tie!")


# add to put number between 1 nd 9
def place_symbol(board):
    while True:
        place = int(input("Place your symbol (1-9): "))
        if board[place] == " ":
            break
        else:
            print("Spot taken!")
    return place


def repeat():
    pass


def game():
    print("Welcome to Tic Tac Toe!")
    p1 = input("Player 1, choose your symbol - X or O: ").upper()

    if p1 == "X":
        p2 = "O"
    else:
        p2 = "X"

    print(f"Player 1: {p1}\nPlayer 2: {p2}")

    board = ["x"] + [" "] * 9

    print("Player 1 starts the game!")

    turn = 1
    time.sleep(1)

    while " " in board:
        show_board(board)

        if turn == 1:
            print("Player 1 turn!")
            index = place_symbol(board)
            board[index] = p1

            if check_win(board, p1):
                show_board(board)
                print("Player 1 won!")
                break
            turn = 2
        else:
            print("Player 2 turn!")
            index = place_symbol(board)
            board[index] = p2

            if check_win(board, p2):
                show_board(board)
                print("Player 2 won!")
                break
            turn = 1


game()
