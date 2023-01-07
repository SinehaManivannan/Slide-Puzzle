import random, sys

BLANK = '  '

def main():
    print('''Slide Puzzle

    Use the WASD Keys.
    Move the tiles into the correct order.
    The tiles should be sorted from lowest to highest when reading 
    from left to right and top to bottom. 
    A solved puzzle should look like the following:
        1  2  3  4 
        5  6  7  8 
        9 10 11 12
       13 14 15
        
    ''')

    input('To start a new game, press Enter!')

    boardOfGame = makeNewPuzzle()

    while 1:
        displayBoard(boardOfGame)
        move = playerMove(boardOfGame)
        makeMove(boardOfGame, move)

        if boardOfGame == freshBoard():
            print('CONGRATS! You won!')
            sys.exit()

def freshBoard():
        """ Return a list of lists that represents a tile puzzle"""
        return [['1 ', '5 ', '9 ', '13'],
                ['2 ', '6 ', '10 ', '14'],
                ['3 ', '7 ', '11', '15'],
                ['4 ', '8 ', '12', BLANK]]

def displayBoard(board):
        """ Display the given board on the screen"""
        labels = [board[0][0], board[1][0], board[2][0], board[3][0],
                  board[0][1], board[1][1], board[2][1], board[3][1],
                  board[0][2], board[1][2], board[2][2], board[3][2],
                  board[0][3], board[1][3], board[2][3], board[3][3]]
        boardDrawn = """
x------x------x------x------x
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
x------x------x------x------x
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
x------x------x------x------x
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
x------x------x------x------x
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
x------x------x------x------x
    """.format(*labels)
        print(boardDrawn)

def findBlankSpace(board):
    """ Return blank space's position """
    for x in range(4):
        for y in range(4):
            if board[x][y] == '  ':
                return (x,y)

def playerMove(board):
        """ Player selects a tile to slide """
        blankx, blanky = findBlankSpace(board)

        s = 'S' if blanky != 3 else ' '
        d = 'D' if blankx != 3 else ' '
        w = 'W' if blanky != 0 else ' '
        a = 'A' if blankx != 0 else ' '

        while True:
            print('Enter WASD (or QUIT): ')

            playerResponse = input('> ').upper()
            if playerResponse == 'QUIT':
                sys.exit()
            if playerResponse in (a + w + s + d).replace(' ', ''):
                return playerResponse

def makeMove(board, move):
            """ Carry out the given move on the given board """
            # Note: This fn assumes that the move is valid.
            bx, by = findBlankSpace(board)

            if move == 'S':
                board[bx][by], board[bx][by + 1] = board[bx][by + 1], board[bx][by]
            elif move == 'D':
                board[bx][by], board[bx + 1][by] = board[bx + 1][by], board[bx][by]
            elif move == 'W':
                board[bx][by], board[bx][by - 1] = board[bx][by - 1], board[bx][by]
            elif move == 'A':
                board[bx][by], board[bx - 1][by] = board[bx - 1][by], board[bx][by]

def randomMove(board):
        """ Slide randomly """
        blankx, blanky = findBlankSpace(board)
        validMoves = []
        if blanky != 3:
            validMoves.append('S')
        if blankx != 3:
            validMoves.append('D')
        if blanky != 0:
            validMoves.append('W')
        if blankx != 0:
            validMoves.append('A')

        makeMove(board, random.choice(validMoves))
        
def makeNewPuzzle(moves=200):
    """ Get a New Puzzle by random slides from the solved position """        
    board = freshBoard()

    for x in range(moves):
        randomMove(board)
    return board

        # If program run then run the game
if __name__ == '__main__':
    main()
