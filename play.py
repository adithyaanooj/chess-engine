import chess
from main import search


print("Welcome. To play, please enter your moves in UCI engine format. E.g: In the starting position, e2 would be e2e4, Nf3 would be g1f3")

board = chess.Board()
while(not(board.is_game_over())):
    move = str(input("Enter move:"))
    board.push_uci(move)
    engineMove, evaluation = search(4, board)
    board.push(engineMove)
    print("Engine moved " + str(engineMove))
    print("Evaluation is " + str(round(evaluation, 3)))

if(board.outcome().result() == "1-0"):
    print("White wins")
elif(board.outcome().result() == "0-1"):
    print("Black wins")
else:
    print("Game drawn")