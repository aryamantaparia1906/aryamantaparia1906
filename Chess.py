import copy
import random
from cmu_112_graphics import * 

def colourList(): 
    #https://www.webucator.com/article/python-color-constants-module/
    #edited and handpicked myself to get the required appropriate colours
    return ['aliceblue', 'antiquewhite', 'aqua', 'azure', 'beige', 'bisque', 
            'blue', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 
            'chocolate', 'coral', 'crimson', 'cyan', 'forestgreen', 'gold', 
            'gray', 'green', 'honeydew', 'indigo', 'ivory', 'khaki', 'lavender',
            'lawngreen', 'lightblue', 'magenta', 'maroon','navy', 'olive', 
            'orange', 'orchid', 'pink', 'plum', 'purple', 'red','royalblue', 
            'sandybrown', 'silver', 'skyblue', 'snow', 'tan', 'tomato', 
            'turquoise', 'violet', 'wheat', 'white', 'yellow']	

def emptyBoard(): #emoty board with 8 rows and cols
    L = []
    for row in range(8):
        L += [[None]*8]
    return L
            
def startingBoard():
    #wP, bP = White Pawn, Black Pawn
    #wR, bR = White Rook, Black Rook
    #wN, bN = White Knight, Black Knight
    #wB, bB = White Bishop, Black Bishop
    #wQ, bQ = White Queen, Black Queen
    #wK, bK = White King, Black King
    return [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],]

def whitePieces(): #list of white pieces
    return ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK']

def blackPieces(): #list of black pieces
    return ['bP', 'bR', 'bN', 'bB', 'bQ', 'bK']

def kingIsBetweenTheRooks(L): #checks if the king is in between the two rooks
    rook1 = None
    rook2 = None
    king = None
    for i in range(len(L)):
        if L[i] == 'wR' and rook1 == None:
            rook1 = i
        elif L[i] == 'wR':
            rook2 = i
        elif L[i] == 'wK':
            king = i
    if rook1 < king and king < rook2:
        return True
    return False

def bishopIsOnDifferentDiagonals(L): 
    #checks if the bishops are on different coloured squares
    bishop1 = None
    bishop2 = None
    for i in range(len(L)):
        if L[i] == 'wB' and bishop1 == None:
            bishop1 = i
        elif L[i] == 'wB':
            bishop2 = i
    if bishop1%2 != bishop2%2:
        return True
    return False

def mirrorWhite(L): #arranges black pieces to be the same as white pieces
    result = []
    for piece in L:
        if piece == 'wR':
            result.append('bR')
        elif piece == 'wN':
            result.append('bN')
        elif piece == 'wB':
            result.append('bB')
        elif piece == 'wQ':
            result.append('bQ')
        elif piece == 'wK':
            result.append('bK')
        elif piece == 'wB':
            result.append('bB')
        elif piece == 'wN':
            result.append('bN')
        elif piece == 'wR':
            result.append('bR')
    return result
            
def chess960StartingBoard(): #starting board of chess 960 game 
    #we rearrange so that bishops have different diagonals, 
    #king is between the two rooks
    #black pieces are placed equal and opposite to white pieces 
    wL = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
    random.shuffle(wL)
    while True:
        if kingIsBetweenTheRooks(wL) and bishopIsOnDifferentDiagonals(wL):
            break #if the board is correct
        random.shuffle(wL)
    bL = mirrorWhite(wL)
    return [bL, #black pieces without pawns arranged
           ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
           [None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None],
           ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'], 
           wL] #white pieces without pawns arranged

def flipBoard(app): #flips the board for player 2's turn
    currBoard = app.board #makes a 2d list of the same dimensions
    newBoard = emptyBoard()
    for row in range(len(newBoard)):
        for col in range(len(newBoard[0])):
            newBoard[row][col] = currBoard[7-row][7-col] 
    app.board = newBoard  #makes app.board into newBoard

def boardPictures(app): 
    #loads and modifies the size of all the piece pics along with style
    #https://opengameart.org/content/pixel-chess-pieces
    #https://drive.google.com/drive/folders/1qH7IQj5lj7o3MQIb5TAZhsDr_5f9p8aq
    if app.pieceStyle == 1:
        app.whitePawn = app.loadImage('wPawn.png')
        app.whiteRook = app.loadImage('wRook.png')
        app.whiteKnight = app.loadImage('wKnight.png')
        app.whiteBishop = app.loadImage('wBishop.png')
        app.whiteQueen = app.loadImage('wQueen.png')
        app.whiteKing = app.loadImage('wKing.png')
        app.blackPawn = app.loadImage('bPawn.png')
        app.blackRook = app.loadImage('bRook.png')
        app.blackKnight = app.loadImage('bKnight.png')
        app.blackBishop = app.loadImage('bBishop.png')
        app.blackQueen = app.loadImage('bQueen.png')
        app.blackKing = app.loadImage('bKing.png')
    if app.pieceStyle == 2:
        app.whitePawnTemp = app.loadImage('pawn.png')
        app.whitePawn = app.scaleImage(app.whitePawnTemp, 1.1)
        app.whiteRookTemp = app.loadImage('rook.png')
        app.whiteRook = app.scaleImage(app.whiteRookTemp, 1.1)
        app.whiteKnightTemp = app.loadImage('knight.png')
        app.whiteKnight = app.scaleImage(app.whiteKnightTemp, 1.1)
        app.whiteBishopTemp = app.loadImage('bishop.png')
        app.whiteBishop = app.scaleImage(app.whiteBishopTemp, 1.1)
        app.whiteQueenTemp = app.loadImage('queen.png')
        app.whiteQueen = app.scaleImage(app.whiteQueenTemp, 1.1)
        app.whiteKingTemp = app.loadImage('king.png')
        app.whiteKing = app.scaleImage(app.whiteKingTemp, 1.1)
        app.blackPawnTemp = app.loadImage('pawn1.png')
        app.blackPawn = app.scaleImage(app.blackPawnTemp, 1.1)
        app.blackRookTemp = app.loadImage('rook1.png')
        app.blackRook = app.scaleImage(app.blackRookTemp, 1.1)
        app.blackKnightTemp = app.loadImage('knight1.png')
        app.blackKnight = app.scaleImage(app.blackKnightTemp, 1.1)
        app.blackBishopTemp = app.loadImage('bishop1.png')
        app.blackBishop = app.scaleImage(app.blackBishopTemp, 1.1)
        app.blackQueenTemp = app.loadImage('queen1.png')
        app.blackQueen = app.scaleImage(app.blackQueenTemp, 1.1)
        app.blackKingTemp = app.loadImage('king1.png')
        app.blackKing = app.scaleImage(app.blackKingTemp, 1.1)

def selfPieceTouch(app, row, col): #checks if a piece hits its own piece
    if row < 0 or col < 0 or row > 7 or col > 7:
        return False
    if app.playerTurn == 'white':
        if app.board[row][col] in whitePieces():
            return True
    elif app.playerTurn == 'black':
        if app.board[row][col] in blackPieces():
            return True
    return False

def opponentPieceTouch(app, row, col): #checks if a pc captures opponent piece
    if row < 0 or col < 0 or row > 7 or col > 7:
        return False
    if app.playerTurn == 'white':
        if app.board[row][col] in blackPieces():
            return True
    else:
        if app.board[row][col] in whitePieces():
            return True
    return False

def pieceTouch(app, row, col): #checks if a piece touches any other piece
    if selfPieceTouch(app, row, col) or opponentPieceTouch(app, row, col):
        return True
    return False

def moveLeadsToCheck(app, oldRow, oldCol, newRow, newCol): 
    #checks that if a move is made, does it result in a check
    prevVal = app.board[oldRow][oldCol]
    nextVal = app.board[newRow][newCol]
    app.board[oldRow][oldCol] = None
    app.board[newRow][newCol] = prevVal
    if check(app):
        app.board[oldRow][oldCol] = prevVal
        app.board[newRow][newCol] = nextVal
        return True
    app.board[oldRow][oldCol] = prevVal
    app.board[newRow][newCol] = nextVal
    return False

def moveIsLegal(app, range): 
    #removes values from the range when a move is touching any of its own pieces
    result = []
    for value in range:
        row = value[0]
        col = value[1]
        if not selfPieceTouch(app, row, col):
            result += [value]
    return result

def removeCheckMoves(app, oldRow, oldCol, range): 
    #removes all possible moves that result in a check
    result = []
    for value in range:
        newRow = value[0]
        newCol = value[1]
        if not moveLeadsToCheck(app, oldRow, oldCol, newRow, newCol):
            result += [value]
    return result

def pawnRange(app, row, col): #pawns attack range
    L = []
    if pieceTouch(app, row-1, col+1): #if pawn can capture right piece
        L += [(row-1, col+1)]
    if pieceTouch(app, row-1, col-1):  #if pawn can capture left piece
        L += [(row-1, col-1)]
    return L

def pawnMovesPossible(app, row, col): #list of all squares the pawn can move
    L = copy.deepcopy(pawnRange(app, row, col))
    if row == 6: #means pawn can double move
        if (not pieceTouch(app, row-1, col) and 
          (not pieceTouch(app, row-2, col))): #pawn can move both squares
           L += [(row-1, col), (row-2, col)]
        elif not pieceTouch(app, row-1, col): #pawn can only move one square
            L += [(row-1, col)]
    else:
        if not pieceTouch(app, row-1, col): #pawn can only move one square
            L += [(row-1, col)]   
    L = moveIsLegal(app, L)
    L = removeCheckMoves(app, row, col, L)
    return L

def knightRange(row, col): #knights attack range
    L = []
    possibleMoves = [(row+1, col+2), (row+1, col-2), (row-1, col+2), 
                    (row-1, col-2), (row+2, col+1), (row+2, col-1), 
                    (row-2, col+1), (row-2, col-1)]
    for move in possibleMoves:
        row = move[0]
        col = move[1]
        if row >= 0 and col >= 0 and row < 8 and col < 8:
            L += [move]
    return L 

def knightMovesPossible(app, row, col): #list of all squares the knight can move
    L = copy.deepcopy(knightRange(row, col))
    L = moveIsLegal(app, L)
    L = removeCheckMoves(app, row, col, L)
    return L

def bishopRange(app, row, col): #bishops attack range
    L = []
    northWest = []
    northEast = []
    southWest = []
    southEast = []
    for i in range(1, 8):
        northWest += [(row-i, col-i)]
        northEast += [(row-i, col+i)]
        southWest += [(row+i, col-i)]
        southEast += [(row+i, col+i)]
    for move in northWest:
        rowNum = move[0]
        colNum = move[1]
        if rowNum >= 0 and colNum >= 0:
            L += [move]
        if pieceTouch(app, rowNum, colNum):
            break
    for move in northEast:
        rowNum = move[0]
        colNum = move[1]
        if rowNum >= 0 and colNum < 8:
            L += [move]
        if pieceTouch(app, rowNum, colNum):
            break
    for move in southWest:
        rowNum = move[0]
        colNum = move[1]
        if rowNum < 8 and colNum >= 0:
            L += [move]
        if pieceTouch(app, rowNum, colNum):
            break
    for move in southEast:
        rowNum = move[0]
        colNum = move[1]
        if rowNum < 8 and colNum < 8:
            L += [move]
        if pieceTouch(app, rowNum, colNum):
            break  
    return L

def bishopMovesPossible(app, row, col): #list of all squares the bishop can move
    L = copy.deepcopy(bishopRange(app, row, col))
    L = moveIsLegal(app, L)
    L = removeCheckMoves(app, row, col, L)
    return L

def rookRange(app, row, col): #rooks attack range
    L = []
    up = row - 1
    down = row + 1
    left = col - 1
    right = col + 1
    while up >= 0:
        L += [(up, col)]
        if pieceTouch(app, up, col):
            break
        up -= 1
    while down < 8:
        L += [(down, col)]
        if pieceTouch(app, down, col):
            break
        down += 1
    while left >= 0:
        L += [(row, left)]
        if pieceTouch(app, row, left):
            break
        left -= 1
    while right < 8:
        L += [(row, right)]
        if pieceTouch(app, row, right):
            break
        right += 1
    return L

def rookMovesPossible(app, row, col): #list of all squares the rook can move
    L = copy.deepcopy(rookRange(app, row, col))
    L = moveIsLegal(app, L)
    L = removeCheckMoves(app, row, col, L)
    return L

def queenRange(app, row, col): #queens attack range
    return rookRange(app, row, col) + bishopRange(app, row, col)

def queenMovesPossible(app, row, col): #list of all squares the queen can move
    L = copy.deepcopy(queenRange(app, row, col))
    L = moveIsLegal(app, L)
    L = removeCheckMoves(app, row, col, L)
    return L

def kingRange(row, col): #kings attack range
    L = []
    possibleMoves = [(row+1, col), (row+1, col+1), (row+1, col-1), (row, col+1), 
            (row, col-1), (row-1, col), (row-1, col+1), (row-1, col-1)]
    for move in possibleMoves:
        row = move[0]
        col = move[1]
        if row >= 0 and col >= 0 and row < 8 and col < 8:
           L += [move]
    return L

def kingMovesPossible(app, row, col): #list of all squares the king can move
    result = []
    opponentRanges = allOpponentRanges(app)
    board = app.board
    L = copy.deepcopy(kingRange(row, col))
    for value in L:
        if (value not in allOpponentRanges(app) and 
            (not selfPieceTouch(app, value[0], value[1]))):
            result += [value]
    if app.playerTurn == 'white': #these moves are for castling
        if app.whiteKingHasMoved == False and app.whiteRookHasMoved == False:
            if ((7,4) not in opponentRanges and board[7][5] == None and 
               (7,5) not in opponentRanges and board[7][6] == None and 
               (7,6) not in opponentRanges and board[7][7] == 'wR'):
               result += [(7, 6)]
            if ((7,4) not in opponentRanges and board[7][3] == None and 
                (7,3) not in opponentRanges and board[7][2] == None and 
                (7,2) not in opponentRanges and board[7][1] == None and
                board[7][0] == 'wR'):
                result += [(7, 2)] #all rules for castling are included
    else:  #these moves are for castling
        if app.blackKingHasMoved == False and app.blackRookHasMoved == False:
            if ((7,3) not in opponentRanges and board[7][2] == None and 
               (7,2) not in opponentRanges and board[7][1] == None and 
               (7,1) not in opponentRanges and board[7][0] == 'bR'):
               result += [(7, 1)]
            if ((7,3) not in opponentRanges and board[7][4] == None and 
                (7,4) not in opponentRanges and board[7][5] == None and 
                (7,5) not in opponentRanges and board[7][6] == None and
                board[7][7] == 'bR'):
                result += [(7, 5)] #all rules for castling are included
    result = removeCheckMoves(app, row, col, result)
    return result

def removeDuplicates(L): #helps remove duplicates for allOpponentRanges(app)
    result = []
    seen = set()
    for value in L:
        if value not in seen:
            result += [value]
            seen.add(value)
    return result

def allOpponentRanges(app): #all the squares the opponent is attacking
    L = []
    board = copy.deepcopy(app.board)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if app.playerTurn == 'white':
                if board[row][col] == 'bN':
                    L += knightRange(row, col)
                elif board[row][col] == 'bB':
                    L += bishopRange(app, row, col)
                elif board[row][col] == 'bK':
                    L += kingRange(row, col)
                elif board[row][col] == 'bQ':
                    L += queenRange(app, row, col)
                elif board[row][col] == 'bP':
                    L += pawnRange(app, row, col)
                elif board[row][col] == 'bR':
                    L += rookRange(app, row, col)
            else:
                if board[row][col] == 'wN':
                    L += knightRange(row, col)
                elif board[row][col] == 'wB':
                    L += bishopRange(app, row, col)
                elif board[row][col] == 'wK':
                    L += kingRange(row, col)
                elif board[row][col] == 'wQ':
                    L += queenRange(app, row, col)
                elif board[row][col] == 'wP':
                    L += pawnRange(app, row, col)
                elif board[row][col] == 'wR':
                    L += rookRange(app, row, col)
    L = removeDuplicates(L)
    return L

def isLegalMove(app): #determines if piece should be placed or not
    board = app.board
    oldRow = app.pieceSelect[0]
    oldCol = app.pieceSelect[1]
    newRow = app.piecePlace[0]
    newCol = app.piecePlace[1]
    if board[oldRow][oldCol] == 'wN' or board[oldRow][oldCol] == 'bN':
        range = copy.deepcopy(knightMovesPossible(app, oldRow, oldCol))
    elif board[oldRow][oldCol] == 'wB' or board[oldRow][oldCol] == 'bB':
        range = copy.deepcopy(bishopMovesPossible(app, oldRow, oldCol))
    elif board[oldRow][oldCol] == 'wK' or board[oldRow][oldCol] == 'bK':
        range = copy.deepcopy(kingMovesPossible(app, oldRow, oldCol))
    elif board[oldRow][oldCol] == 'wQ' or board[oldRow][oldCol] == 'bQ':
        range = copy.deepcopy(queenMovesPossible(app, oldRow, oldCol))
    elif board[oldRow][oldCol] == 'wP' or board[oldRow][oldCol] == 'bP':
        range = copy.deepcopy(pawnMovesPossible(app, oldRow, oldCol))
    elif board[oldRow][oldCol] == 'wR' or board[oldRow][oldCol] == 'bR':
        range = copy.deepcopy(rookMovesPossible(app, oldRow, oldCol))
    if (newRow, newCol) in range:
        return True
    return False

def findKing(app): #finds the position of the king to determine check
    board = copy.deepcopy(app.board)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if app.playerTurn == 'white':
                if board[row][col] == 'wK':
                    return (row, col)
            else:
                if board[row][col] == 'bK':
                    return (row, col)
                    
def noPossibleMove(app, row, col):
    board = copy.deepcopy(app.board)
    if board[row][col] == 'wN' or board[row][col] == 'bN':
        if knightMovesPossible(app, row, col) == []:
            return True
    elif board[row][col] == 'wB' or board[row][col] == 'bB':
        if bishopMovesPossible(app, row, col) == []:
            return True
    elif board[row][col] == 'wK' or board[row][col] == 'bK':
        if kingMovesPossible(app, row, col) == []:
            return True
    elif board[row][col] == 'wQ' or board[row][col] == 'bQ':
        if queenMovesPossible(app, row, col) == []:
            return True
    elif board[row][col] == 'wP' or board[row][col] == 'bP':
        if pawnMovesPossible(app, row, col) == []:
            return True
    elif board[row][col] == 'wR' or board[row][col] == 'bR':
        if rookMovesPossible(app, row, col) == []:
            return True
    return False

def stalemate(app):
    board = copy.deepcopy(app.board)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if app.playerTurn == 'white':
                if board[row][col] == 'wN':
                    if knightMovesPossible(app, row, col) != []:
                        return False
                elif board[row][col] == 'wB':
                    if bishopMovesPossible(app, row, col) != []:
                        return False
                elif board[row][col] == 'wK':
                    if kingMovesPossible(app, row, col) != []:
                        return False
                elif board[row][col] == 'wQ':
                    if queenMovesPossible(app, row, col) != []:
                        return False
                elif board[row][col] == 'wP':
                    if pawnMovesPossible(app, row, col) != []:
                        return False
                elif board[row][col] == 'wR':
                    if rookMovesPossible(app, row, col) != []:
                        return False
            else:
                if board[row][col] == 'bN':
                    if knightMovesPossible(app, row, col) != []:
                        return False
                elif board[row][col] == 'bB':
                    if bishopMovesPossible(app, row, col) != []:
                        return False
                elif board[row][col] == 'bK':
                    if kingMovesPossible(app, row, col) != []:
                        return False
                elif board[row][col] == 'bQ':
                    if queenMovesPossible(app, row, col) != []:
                        return False
                elif board[row][col] == 'bP':
                    if pawnMovesPossible(app, row, col) != []:
                        return False
                elif board[row][col] == 'bR':
                    if rookMovesPossible(app, row, col) != []:
                        return False
    return True

def castle(app): #moves the rook in the right place after castling
    board = app.board
    oldRow = app.pieceSelect[0]
    oldCol = app.pieceSelect[1]
    newCol = app.piecePlace[1]
    if board[oldRow][oldCol] == 'wK':
        if newCol == oldCol + 2:
            app.board[7][7] = None
            app.board[7][5] = 'wR'
        elif newCol == oldCol - 2:
            app.board[7][0] = None
            app.board[7][3] = 'wR'
    elif board[oldRow][oldCol] == 'bK':
        if newCol == oldCol - 2:
            app.board[7][0] = None
            app.board[7][2] = 'bR'
        elif newCol == oldCol + 2:
            app.board[7][7] = None
            app.board[7][4] = 'bR'

def pieceHasMoved(app): #castling condition
    row = app.pieceSelect[0]
    col = app.pieceSelect[1]
    piece = app.board[row][col]
    if piece == 'wK':
        app.whiteKingHasMoved = True
    elif piece == 'bK':
        app.blackKingHasMoved = True
    elif piece == 'wR':
        app.whiteRookHasMoved = True
    elif piece == 'bR':
        app.blackRookhasMoved = True

def check(app): 
    kingPosition = findKing(app)  
    if kingPosition in allOpponentRanges(app):
        return True
    return False

def checkmate(app):
    kingPosition = findKing(app)
    kingRow = kingPosition[0]
    kingCol = kingPosition[1]
    if (kingMovesPossible(app, kingRow, kingCol) == [] and check(app) == True and
       stalemate(app) == True):
        return True
    return False

def gameOver(app):
    if checkmate(app):
        app.checkmate = True
        app.gameOver = True
    elif stalemate(app):
        app.stalemate = True
        app.gameOver = True   
    elif app.illegalMovesWhite > 1 or app.illegalMovesBlack > 1:
        app.illegalMovesExceeded = True
        app.gameOver = True
    
def pointInGrid(app, x, y): #similar to 112 notes
    #returns True if (x, y) is inside the grid
    return ((app.margin <= x <= app.width-app.margin) and
            (app.margin <= y <= app.height-app.margin))

def getCell(app, x, y): #similar to 112 notes
    #gets the cell row and col given mouse selection
    if (not pointInGrid(app, x, y)):
        return (-1, -1)
    row = int((y - app.margin) / app.squareSize)
    col = int((x - app.margin) / app.squareSize)
    return (row, col)

def makeMove(app):
    prevRow = app.pieceSelect[0]
    prevCol = app.pieceSelect[1]
    nextRow = app.piecePlace[0]
    nextCol = app.piecePlace[1]
    prevVal = app.board[prevRow][prevCol]
    pieceHasMoved(app)
    castle(app)
    app.board[nextRow][nextCol] = prevVal
    app.board[prevRow][prevCol] = None
    if app.playerTurn == 'white':
        app.playerTurn = 'black'
    else:
        app.playerTurn = 'white'
    gameOver(app)
    flipBoard(app) #flips board for next player's turn
    app.pieceSelect = (-1,-1)
    app.piecePlace = (-1,-1) 

def illegalMove(app): #increases count of illegal moves
    if app.playerTurn == 'white': 
        app.illegalMovesWhite += 1
    else:
        app.illegalMovesBlack += 1 

def drawBoard(app, canvas):
    #first draws the outline
    canvas.create_rectangle(app.margin - app.outline, 
                            app.margin - app.outline, 
                            app.width - app.margin + app.outline, 
                            app.height - app.margin + app.outline, 
                            fill = app.outlineColour) 
    #draws the chess board with given colours
    for row in range(8):
        y1 = app.margin +  row * app.squareSize
        y2 = y1 + app.squareSize
        for col in range(8):
            x1 = app.margin + col * app.squareSize
            x2 = x1 + app.squareSize
            if (row+col)%2 == 0:
                colour = app.boardColour1
            else:
                colour = app.boardColour2
            canvas.create_rectangle(x1, y1, x2, y2, fill = colour)

def drawPieces(app, canvas): #draws the pieces acc to current state of board
    for row in range(8):
        for col in range(8):
            piece = app.board[row][col]
            if piece != None:
                x = app.margin + app.squareSize*col + app.squareSize//2, 
                y = app.margin + app.squareSize*row + app.squareSize//2,
                if piece == 'wP':
                    canvas.create_image(x, y, 
                    image=ImageTk.PhotoImage(app.whitePawn))
                elif piece == 'wR':
                    canvas.create_image(x, y, 
                    image=ImageTk.PhotoImage(app.whiteRook))
                elif piece == 'wN':
                    canvas.create_image(x, y, 
                    image=ImageTk.PhotoImage(app.whiteKnight))
                elif piece == 'wB':
                    canvas.create_image(x, y, 
                    image=ImageTk.PhotoImage(app.whiteBishop))
                elif piece == 'wQ':
                    canvas.create_image(x, y, 
                    image=ImageTk.PhotoImage(app.whiteQueen))
                elif piece == 'wK':
                    canvas.create_image(x, y, 
                    image=ImageTk.PhotoImage(app.whiteKing))
                elif piece == 'bP':
                    canvas.create_image(x, y,
                    image=ImageTk.PhotoImage(app.blackPawn))
                elif piece == 'bR':
                    canvas.create_image(x, y,
                    image=ImageTk.PhotoImage(app.blackRook))
                elif piece == 'bN':
                    canvas.create_image(x, y, 
                    image=ImageTk.PhotoImage(app.blackKnight))
                elif piece == 'bB':
                    canvas.create_image(x, y, 
                    image=ImageTk.PhotoImage(app.blackBishop))
                elif piece == 'bQ':
                    canvas.create_image(x, y, 
                    image=ImageTk.PhotoImage(app.blackQueen))
                elif piece == 'bK':
                    canvas.create_image(x, y, 
                    image=ImageTk.PhotoImage(app.blackKing))

def drawText(app, canvas): #draws the numbers and letters of the board
    listOfNums = ['1','2','3','4','5','6','7','8']
    listOfLetters = ['a','b','c','d','e','f','g','h']
    for col in range(8):
        x = app.margin + app.squareSize*col + app.squareSize//2 
        y = app.height - app.margin + app.outline//3
        if app.playerTurn == 'white': 
            canvas.create_text(x, y, text=listOfLetters[col], 
            font="Times 14 bold")          
        else: #if black, it has to be descending letters
            canvas.create_text(x, y, text=listOfLetters[7-col], 
            font="Times 14 bold")
    for row in range(8):
        x = app.margin - app.outline//2
        y = app.margin + app.squareSize*row + app.squareSize//2
        if app.playerTurn == 'white': #if white, it has to be descending nums
            canvas.create_text(x, y, text=listOfNums[7-row], 
            font="Times 14 bold")
        else:
            canvas.create_text(x, y, text=listOfNums[row],
            font="Times 14 bold")

def drawStalemate(app, canvas): #draws the end result if it is a stalemate
    canvas.create_rectangle(0, 0, app.width, app.height//6.8, 
                            fill= 'orange')
    canvas.create_text(app.width//2, app.height//13, 
                      text="Draw.  It's a stalemate!", 
                      font="Times 25 bold", fill='blue')

def drawCheckmate(app, canvas): #draws the result when its a checkmate
    canvas.create_rectangle(0, 0, app.width, app.height//6.8, 
                            fill= 'yellow')
    canvas.create_text(app.width//2, app.height//25, text='Checkmate!',
                      font="Times 28 bold", fill='purple') 
    if app.playerTurn == 'white': #if black wins
        canvas.create_text(app.width//2, app.height//10, text='Black wins.',
                      font="Times 20 bold", fill='green') 
    else: #if white wins
        canvas.create_text(app.width//2, app.height//10, text='White wins.',
                      font="Times 20 bold", fill='green') 
        
def drawIllegalMove(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height//6.8, 
                            fill= 'cyan')
    canvas.create_text(app.width//2, app.height//25, 
                    text='Maximum number of illegal moves exceeded!',
                    font="Times 24 bold", fill='violet') 
    if app.playerTurn == 'white': #if black wins
        canvas.create_text(app.width//2, app.height//10, text='Black wins.',
                      font="Times 20 bold", fill='green') 
    else: #if white wins
        canvas.create_text(app.width//2, app.height//10, text='White wins.',
                      font="Times 20 bold", fill='green')

def gameRules(app):
    app.illegalMovesWhite = 0 #no of illegal moves made by white
    app.illegalMovesBlack = 0 #no of illegal moves made by black
    app.whiteKingHasMoved = False #for checking if white king can castle
    app.blackKingHasMoved = False #for checking if black king can castle
    app.whiteRookHasMoved = False #for white castle check
    app.blackRookHasMoved = False #for black castle check
    app.checkmate = False
    app.stalemate = True
    app.illegalMovesExceeded = False
    app.gameOver = False

def appStarted(app):
    app.board = startingBoard() #chess board 
    app.pieceStyle = 1 #style of the pieces in the board
    boardPictures(app) #all the pictures are loaded
    app.gameMode = 'normal'
    app.boardColour1 = 'white' #first colour of the board
    app.boardColour2 = 'green' #second colour of the board
    app.timerDelay = 1000 #makes timerDelay a second
    app.player1Time = 600 #time left for player 1
    app.player2Time = 600 #time left for player 2
    app.margin = app.width//6 #margin size
    app.squareSize = (app.width - 2*app.margin)//8 #width or height of each sq
    app.outline = app.width//50 #ouline size of the board
    app.outlineColour = 'brown' 
    app.playerTurn = 'white'
    app.pieceSelect = (-1, -1) #selected piece row and col
    app.piecePlace = (-1,-1) #placed piece row and col
    app.allMoves = []
    gameRules(app)

def keyPressed(app, event):
    listOfColours = colourList()
    if event.key == 'r': #if user presses r (for restart)
        appStarted(app)
        listOfColours = colourList()
    elif event.key == 'Right': #if user presses c (for colour)
        while True: 
            #use while loop so that there are always 2 different colours 
            #the colours can also never be the same
            app.boardColour1 = random.choice(listOfColours) 
            app.boardColour2 = random.choice(listOfColours)
            if app.boardColour1 != app.boardColour2:
                break 
        app.pieceStyle = random.randint(1, 2)
        boardPictures(app) 
        app.outlineColour = random.choice(listOfColours)
    elif event.key == 'b': #if user presses b (for chess960)
        app.board = chess960StartingBoard()
        app.gameMode = 'chess960'
        app.pieceSelect = (-1,-1)
        app.piecePlace = (-1,-1)
        app.playerTurn = 'white'
    elif event.key == 'n': #if user presses n (for normal mode)
        app.board = startingBoard()
        app.gameMode = 'normal'
        app.pieceSelect = (-1,-1)
        app.piecePlace = (-1,-1)
        app.playerTurn = 'white'
    elif event.key == 'f':
        flipBoard(app)
        
def mousePressed(app, event):
    (row, col) = getCell(app, event.x, event.y) #touch and move!
    if app.pieceSelect != (-1,-1) and app.pieceSelect != (row, col):
        app.piecePlace = (row, col) 
        if isLegalMove(app):
            makeMove(app)
        else: #if it is an illegal move
            illegalMove(app)
            gameOver(app)
            app.piecePlace = (-1,-1) #user is allowed to place again
    else:
        if app.playerTurn == 'white': #so that user cannot select a wrong piece
            if app.board[row][col] in whitePieces(): 
                app.pieceSelect = (row, col)
        else:
            if app.board[row][col] in blackPieces():
                app.pieceSelect = (row, col)
        if noPossibleMove(app, row, col):
            illegalMove(app)
            gameOver(app)
            app.pieceSelect = (-1,-1) #user can reselect again

def redrawAll(app, canvas):
    drawBoard(app, canvas)
    drawPieces(app, canvas)
    drawText(app, canvas)
    if app.stalemate:
        drawStalemate(app, canvas)
    if app.checkmate:
        drawCheckmate(app, canvas)
    if app.illegalMovesExceeded:
        drawIllegalMove(app, canvas)

runApp(width=800, height=800)