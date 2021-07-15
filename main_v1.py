import chess
import math
inf = math.inf
'''
Conventions used:
turn - 1 implies white, 0 implies black -- board.turn 
gamePhase - 0 opening, 1 middlegame, 2 endgame
'''

material_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3.5,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 50
}

pieceSquareWhitePawn = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0.05, 0.05, 0.1, -0.2, -0.2, 0.1, 0.1, 0.05,
    0.05, 0.05, -0.2, 0, 0, -0.1, 0.025, 0.05,
    0, -0.1, 0, 0.2, 0.2, 0.1, -0.1, 0,
    0.05, 0.05, 0.1, 0.25, 0.25, 0.1, 0.05, 0.05,
    0.1, 0.1, 0.2, 0.3, 0.3, 0.2, 0.1, 0.1,
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    0, 0, 0, 0, 0, 0, 0, 0 
]
pieceSquareWhiteKnight = [
    -0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5,
    -0.4, -0.2, 0, 0, 0, 0, -0.2, -0.4,
    -0.3, 0, 0.1, 0.15, 0.15, 0.1, 0, -0.3,
    -0.3, 0.05, 0.15, 0.2, 0.2, 0.15, 0.05, -0.3, 
    -0.3, 0, 0.15, 0.2, 0.2, 0.15, 0, -0.3,
    -0.3, 0.05, 0.10, 0.15, 0.15, 0.10, 0.05, -0.3,
    -0.4, -0.2, 0, 0.05, 0.05, 0, -0.2, -0.4,
    -0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5
]

pieceSquareWhiteBishop = [
    -0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2,
    -0.1, 0.05, 0, 0, 0, 0, 0.05, -0.1,
    -0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.1,
    -0.1, 0, 0.1, 0.1, 0.1, 0.1, 0, -0.1,
    -0.1, 0.05, 0.05, 0.1, 0.1, 0.05, 0.05, -0.1,
    -0.1, 0, 0.05, 0.1, 0.1, 0.05, 0, -0.1,
    -0.1, 0, 0, 0, 0, 0, 0, -0.1,
    -0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2
]
pieceSquareWhiteRook = [
    0, 0, 0, 0.05, 0.05, 0, 0, 0,
    -0.05, 0, 0, 0, 0, 0, 0, -0.05,
    -0.05, 0, 0, 0, 0, 0, 0, -0.05,
    -0.05, 0, 0, 0, 0, 0, 0, -0.05,
    -0.05, 0, 0, 0, 0, 0, 0, -0.05,
    -0.05, 0, 0, 0, 0, 0, 0, -0.05,
    -0.05, 0, 0, 0, 0, 0, 0, -0.05,
    0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05
]

pieceSquareWhiteQueen = [
    -0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2,
    -0.1, 0, 0, 0, 0, 0, 0, -0.1,
    -0.1, 0, 0.05, 0.05, 0.05, 0.05, 0, -0.1,
    -0.05, 0, 0.05, 0.05, 0.05, 0.05, 0, -0.05,
    0, 0, 0.05, 0.05, 0.05, 0.05, 0, -0.05,
    -0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0, -0.1,
    -0.1, 0, 0.05, 0, 0, 0, 0, -0.1,
    -0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2 
]

pieceSquareWhiteKing = [
    0.2, 0.3, 0.1, 0, 0, 0.1, 0.3, 0.2,
    0.2, 0.2, 0, 0, 0, 0, 0.2, 0.2,
    -0.1, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.1,
    -0.2, -0.3, -0.3, -0.4, -0.4, -0.3, -0.3, -0.2,
    -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3,
    -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3,
    -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3,
    -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3
]

pieceSquareBlackPawn = list(reversed(pieceSquareWhitePawn))
pieceSquareBlackKnight = list(reversed(pieceSquareWhiteKnight))
pieceSquareBlackBishop = list(reversed(pieceSquareWhiteBishop))
pieceSquareBlackRook = list(reversed(pieceSquareWhiteRook))
pieceSquareBlackQueen = list(reversed(pieceSquareWhiteQueen))
pieceSquareBlackKing = list(reversed(pieceSquareWhiteKing))


def pieceSquareValue(square, piece, gamePhase):
    if piece.piece_type == chess.PAWN:
        if piece.color == chess.WHITE:
            return pieceSquareWhitePawn[square]
        else:
            return pieceSquareBlackPawn[square]
    elif piece.piece_type == chess.BISHOP:
        if piece.color == chess.WHITE:
            return pieceSquareWhiteBishop[square]
        else:
            return pieceSquareBlackBishop[square]
    elif piece.piece_type == chess.KNIGHT:
        if piece.color == chess.WHITE:
            return pieceSquareWhiteKnight[square]
        else:
            return pieceSquareBlackKnight[square]
    elif piece.piece_type == chess.ROOK:
        if piece.color == chess.WHITE:
            return pieceSquareWhiteRook[square]
        else:
            return pieceSquareBlackRook[square]
    elif piece.piece_type == chess.QUEEN:
        if piece.color == chess.WHITE:
            return pieceSquareWhiteQueen[square]
        else:
            return pieceSquareBlackQueen[square]
    else:
        if piece.color == chess.WHITE:
            return pieceSquareWhiteKing[square]
        else:
            return pieceSquareBlackKing[square]


def pieceCount(board):
    #(p, P, n, N, b, B, r, R, q, Q) 
    count = (0,0,0,0,0,0,0,0,0,0)
    for square in chess.SQUARES:
        piece = board.piece_at(square)
    return count
def evaluateMaterial(board):
    if(board.is_game_over()):
        if board.outcome().result() == "1-0":
            return (inf)
        elif board.outcome().result() == "0-1":
            return -(inf)
        else:
            return 0
    white_eval, black_eval = (0.0, 0.0)
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        #print(square)
        if(not(piece is None)):
            if piece.color == chess.WHITE:
                white_eval+= (material_values[piece.piece_type]+pieceSquareValue(square, piece, 0))
            else:
                black_eval+=(material_values[piece.piece_type]+pieceSquareValue(square, piece, 0))
    return white_eval - black_eval


def eval(board):
    white_eval = 0
    black_eval = 0
    return evaluateMaterial(board)

def bestMoveOrder(board: chess.Board):
    legalMoves = (board.legal_moves)
    def comparator(move):
        board.push(move)
        evaluation = eval(board)
        board.pop()
        return evaluation
    bestMoves = sorted(legalMoves, key = comparator, reverse = board.turn==chess.WHITE)
    return list(bestMoves)

def alphaBetaPruning(board:chess.Board, depth, alpha=(-inf), beta=(+inf)):
    turn = board.turn
    if(board.is_game_over()):
        if board.outcome().result() == "1-0":
            return (inf)
        elif board.outcome().result() == "0-1":
            return -(inf)
        else:
            return 0
    if(depth == 0):
        return eval(board)
    
    if(turn):
        legal = bestMoveOrder(board)
        max_eval = -(inf)
        for move in legal:
            board.push(move)
            max_eval = max(max_eval, alphaBetaPruning(board, depth-1, alpha, beta))
            board.pop()
            if max_eval >=alpha:
                alpha = max_eval
            if beta <=alpha:
                return max_eval
        return max_eval
    else:
        legal = bestMoveOrder(board)
        min_eval = (inf)
        for move in legal:
            board.push(move)
            min_eval = min(min_eval, alphaBetaPruning(board, depth-1, alpha, beta))
            board.pop()
            if min_eval <= beta:
                beta = min_eval
            if beta <=alpha:
                return min_eval
        return min_eval

def search(depth, board):
    turn = board.turn
    if turn:
        best_eval = -(inf)
    else:
        best_eval = (inf)
    legal = bestMoveOrder(board)
    best_move = legal[0]
    #print("at depth " + str(depth) + ", " + str(legal))
    for move in legal:
        board.push(move)
        current_eval = alphaBetaPruning(board, depth-1)
        board.pop()
        if((turn and best_eval<=current_eval) or (not turn and best_eval>=current_eval)):
            best_eval = current_eval
            best_move = move
    return (best_move, best_eval)

