from gui.graphicsDisplay import GraphicsPuzzle
from gameState import EightPuzzleState
import searchStrategy

def main():
    # puzzle_game = GraphicsPuzzle()
    # puzzle_game.start()

    puzzle = EightPuzzleState()
    search = searchStrategy.Search()

if __name__ == '__main__':
    main()
