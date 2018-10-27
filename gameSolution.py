class GameSolution:
    """
        A class holding the final solution of search algorithm.
        :attr path : list of states visited to reach the game solution
        :attr max_depth : maximum depth reached in the search tree
    """
    def __init__ (self, goalState, max_depth=0, no_of_nodes=0):
        self.path = []
        self.max_depth = max_depth
        self.no_of_nodes = no_of_nodes
        self.build_game_solution(goalState)

    def build_game_solution(self, goalState):
        """
        Builds the path list by tracing the goalState up to the initialState.

        :param goalState: The goal state reached by the search algorithm
        """
        stateIterator = goalState
        # trace path to initial state and add them to path list
        while stateIterator != None:
            self.path.append(stateIterator)
            stateIterator = stateIterator.parent
        self.path = self.path[::-1] # reverse path

    def print_game_solution(self):
        """
        Prints the contents of the game solution.
        """
        # print path
        for state in self.path:
            state.print_board()
        # print max_depth
        print('Max Depth reached : ' + str(self.max_depth))
        # print path length
        print('Total Path length : ' + str(len(self.path)))
        #print no_of_nodes_expanded
        print('Total no of nodes : ' + str(self.no_of_nodes))