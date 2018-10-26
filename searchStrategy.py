
from gameSolution import GameSolution
from gameState import EightPuzzleState
import container
import queue
import heuristics

class Search:

    def breadth_first_search(self, gameState):
        return self.generic_graph_search(gameState, container.Queue())

    def depth_first_search(self, gameState):
        return self.generic_graph_search(gameState, container.Stack())

    def a_star_search(self, gameState):
        cost_function = lambda x : heuristics.get_heuristic_cost(x, 'manhattan')  
        return self.generic_graph_search(gameState, container.PriorityQueue(cost_function))
    
    def generic_graph_search(self, gameState, container):
        container.put_element(gameState)
        max_depth = 0
        visited = set()
        while container.is_empty() == False:
          current = container.get_element()
          max_depth = max(max_depth, current.depth)
          if current.is_goal():
            return GameSolution(current, max_depth)
          visited.add(current.get_state_string())
          moves = current.get_successor_moves()
          moves = moves[::-1]
          for move in moves:
            adjacentState = current.apply_move(move)
            adjacentState.parent = current
            adjacentState.depth = current.depth + 1
            if adjacentState.get_state_string() not in visited:
              container.put_element(adjacentState)
        return GameSolution(None)


def main():
    puzzle = EightPuzzleState([3, 1, 2, 0, 4, 5, 6, 7, 8])
    
    search = Search()

    
    # gameSolution = search.breadth_first_search(puzzle)
    # gameSolution.print_game_solution()

    # gameSolution = search.depth_first_search(puzzle)
    # gameSolution.print_game_solution()

    gameSolution = search.a_star_search(puzzle)
    gameSolution.print_game_solution()

if __name__ == '__main__':
    main()
