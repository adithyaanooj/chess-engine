import chess
import math
from main import eval, search, bestMoveOrder

#board = chess.Board("2q3k1/8/8/5N2/6P1/7K/8/8 w - - 0 1")
#LEGALS MATE
#board = chess.Board("r2qkbnr/ppp2ppp/2np4/4N3/2B1P3/2N4P/PPPP1PP1/R1BbK2R w KQkq - 0 1")
#board.push_san("f3")
#board.push_san("e5")
#board.push_san("g4")
#board.push_san("Bc5")
#board.push_san("Qh5")
#board.push_san("Nf6")
board = chess.Board("1k5r/pP3ppp/3p2b1/1BN1n3/1Q2P3/P1B5/KP3P1P/7q w - - 1 0")
#print(eval(board))
print(search(6, board))
#print(eval(board))
#print(bestMoveOrder(board))