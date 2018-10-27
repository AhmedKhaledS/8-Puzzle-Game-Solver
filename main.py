from gui.graphicsDisplay import GraphicsPuzzle
from gameState import EightPuzzleState
import time
from searchStrategy import Search


def main():
    #8, 0, 2, 4, 5, 6, 1, 3, 7
    puzzle = EightPuzzleState([2, 4, 1, 3, 8, 0, 6, 7, 5])
    search = Search()
    print('Game Puzzle:')
    puzzle.print_board()
    start_time = time.time()
    gameSolution = search.a_star_search(puzzle, 'euclidean')
    gameSolution.print_game_solution()
    end_time = time.time()
    print('Running time: {} seconds'.format(end_time - start_time))

    graphics = GraphicsPuzzle()
    graphics.show(gameSolution)

if __name__ == '__main__':
    main()
