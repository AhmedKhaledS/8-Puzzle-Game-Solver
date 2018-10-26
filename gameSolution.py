class GameSolution:

	def __init__ (self, goalState, max_depth=0):
		self.path = []
		self.max_depth = max_depth
		self.build_game_solution(goalState)

	def build_game_solution(self, goalState):
		stateIterator = goalState
		# trace path to initial state and add them to path list
		while stateIterator != None:
			self.path.append(stateIterator)
			stateIterator = stateIterator.parent
		self.path = self.path[::-1] # reverse path

	def print_game_solution(self):
		# print path
		for state in self.path:
			state.print_board()
		# print max_depth
		print('Max Depth reached : ' + str(self.max_depth))
		# print path length
		print('Total Path length : ' + str(len(self.path)))