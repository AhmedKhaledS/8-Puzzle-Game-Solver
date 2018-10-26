from gui.graphicsDisplay import GraphicsPuzzle
from gameState import EightPuzzleState
import searchStrategy
from searchStrategy import Search


def main():
    puzzle = EightPuzzleState([8, 1, 2, 4, 5, 6, 0, 3, 7])
    search = Search()
    gameSolution = search.a_star_search(puzzle)
    gameSolution.print_game_solution()

    graphics = GraphicsPuzzle()
    graphics.show(gameSolution)

if __name__ == '__main__':
    main()
