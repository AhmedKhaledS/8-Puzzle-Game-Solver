
from gameSolution import GameSolution
from gameState import EightPuzzleState
import container
import queue
import heuristics

class Search:
    """
    Class that presents multiple search strategies to search a state space. 
    """

    def breadth_first_search(self, gameState):
      """
      Breadth First Search approach to search a state space.

      :param gameState: initial game state
      :return: game solution object containing the solution of the game
      """
      return self.generic_graph_search(gameState, container.Queue())

    def depth_first_search(self, gameState):
      """
      Depth First Search approach to search a state space.

      :param gameState: initial game state
      :return: game solution object containing the solution of the game
      """
      return self.generic_graph_search(gameState, container.Stack())

    def a_star_search(self, gameState, heuristic='manhattan'):
      """
      A* Search approach to search a state space using heuristic cost function.

      :param gameState: initial game state
      :param heuristic: the heuristic to be used
      :return: game solution object containing the solution of the game
      """
      cost_function = lambda x : heuristics.get_heuristic_cost(x, heuristic) + x.depth
      return self.generic_graph_search(gameState, container.PriorityQueue(cost_function))
    
    def generic_graph_search(self, gameState, container):
      """
      Generic Graph Search used by any graph search algorithm.

      :param gameState: initial game state
      :param container: the container to hold the frontier list to be visited next
      :return: game solution object containing the solution of the game
      """
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
