import getopt
import sys
import time
import random

# Check if someone has won the game
def checkGameOver(board, round, filleds):

    # For a unk reason PythonAnywhere have a problem with comma-separated prints... So, we need to concat with '+'
    if board[0] == board[1] == board[2] != '_':
        print("Player " + board[0] + " won the game in round " + str(round) + " scoring at the first horizontal line")
    elif board[3] == board[4] == board[5] != '_':
        print("Player " + board[3] + " won the game in round " + str(round) + " scoring at the second horizontal line")
    elif board[6] == board[7] == board[8] != '_':
        print("Player " + board[6] + " won the game in round " + str(round) + " scoring at the third horizontal line")
    elif board[0] == board[3] == board[6] != '_':
        print("Player " + board[0] + " won the game in round " + str(round) + " scoring at the first vertical line")
    elif board[1] == board[4] == board[7] != '_':
        print("Player " + board[1] + " won the game in round " + str(round) + " scoring at the second vertical line")
    elif board[2] == board[5] == board[8] != '_':
        print("Player " + board[2] + " won the game in round " + str(round) + " scoring at the third vertical line")
    elif board[0] == board[4] == board[8] != '_':
        print("Player " + board[0] + " won the game in round " + str(round) + " scoring at the primary diagonal")
    elif board[2] == board[4] == board[6] != '_':
        print("Player " + board[2] + " won the game in round " + str(round) + " scoring at the secondary diagonal")
    else:
        if filleds == 9:
            print("The game ended in a draw. Better lucky next time :)")
        else:
            return
    sys.exit()


def print_board(board):
    board = ''.join(board)
    if len(board) == 9:
        print("           ")
        for line in range(3):
            line_str = ''
            line_bar = ['','|','|']
            for item in board[line*3: line*3+3]:
                if item.upper() == 'X':
                    line_str+=' X '+line_bar.pop()
                elif item.upper() == 'O':
                    line_str+=' O '+line_bar.pop()
                else:
                    line_str+= '   '+line_bar.pop()
            print(line_str)
            if line==2:
                print("           ")
            else:
                print("-----------")

if __name__ == "__main__":
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv,"hf:b:v",["first=","board=","verbose="])
        for opt, arg in opts:
            if opt == '-h':
                print("%s -f x -b ____x____"%(__file__))
                sys.exit()
            elif opt in ("-v", "--verbose"):
                print_board(board)
            elif opt in ("-b", "--board"):
                if len(arg) == 9:
                    board = list(arg)
                else:
                    print("wrong board!")
    except getopt.GetoptError:
        print("%s -f x -b ____x____"%(__file__))
        sys.exit(2)
