from game import Game2048

game = Game2048()
game.state = [4, 0, 0, 2,
              0, 0, 0, 4,
              0, 0, 0, 4,
              4, 0, 0, 0]

game.display_state()
print(game.score)
game.make_move(2)
game.display_state()
print(game.score)