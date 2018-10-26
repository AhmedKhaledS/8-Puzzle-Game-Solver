
from gameSolution import GameSolution
from gameState import EightPuzzleState
import queue

class Search:

    def breadth_first_search(self, gameState):
        bfsQueue = queue.Queue()
        bfsQueue.put(gameState)
        max_depth = 0
        visited = set()
        while bfsQueue.empty() == False:
          current = bfsQueue.get_nowait()
          max_depth = max(max_depth, current.depth)
          if current.is_goal():
            return GameSolution(current, max_depth)
          visited.add(current.get_state_string())
          moves = current.get_successor_moves()
          for move in moves:
            adjacentState = current.apply_move(move)
            adjacentState.parent = current
            adjacentState.depth = current.depth + 1
            if adjacentState.get_state_string() not in visited:
              bfsQueue.put(adjacentState)
        return GameSolution(None)


    def depth_first_search(self, gameState):
        dfsStack = [] # python list suffices as a stack
        dfsStack.append(gameState)
        max_depth = 0
        visited = set()
        while dfsStack:
          current = dfsStack.pop()
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
              dfsStack.append(adjacentState)
        return GameSolution(None)

    def a_star_search(self, gameState):
        pass

    def generic_graph_search(self, gameState):
        pass

def main():
    puzzle = EightPuzzleState([3, 1, 2, 6, 4, 5, 0, 7, 8])
    
    search = Search()
    
    gameSolution = search.breadth_first_search(puzzle)
    gameSolution.print_game_solution()

    gameSolution = search.depth_first_search(puzzle)
    gameSolution.print_game_solution()
if __name__ == '__main__':
    main()
