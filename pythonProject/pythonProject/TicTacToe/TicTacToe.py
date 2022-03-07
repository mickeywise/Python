game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

def game_board():
    print(" a  b  c")
    for count, row in enumerate(game):
        print(row, count)
game_board()

game[0][1] = 1

game_board()


