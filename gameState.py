import sys
class EightPuzzleState:

    def __init__(self, numbers_order=[0, 1, 2, 3, 4, 5, 6, 7, 8]):
        """
         Builds a game board by the given sequence of numbers that match representation below.
        example: [1, 2, 0, 3, 5, 4, 8, 7]

          represents the eight puzzle:
            -------------
            | 1 | 2 |   |
            -------------
            | 3 | 5 | 4 |
            -------------
            | 6 | 8 | 7 |
            ------------
        """
        self.parent = None
        self.depth = 0

        self.board = []
        self.blank_location = 0, 0 # initially
        self._iterator = 0
        for row in range(3):
            self.board.append([])
            for col in range(3):
                self.board[row].append(numbers_order[self._iterator])
                if numbers_order[self._iterator] == 0:
                    self.blank_location = row, col
                self._iterator += 1

    def is_goal(self):
        """
        Checks whether the current state of the board is goal or not.
        :return: bool
        """
        counter_checker = 0
        for row in range(3):
            for col in range(3):
                if self.board[row][col] != counter_checker:
                    return False
                counter_checker += 1
        return True

    def apply_move(self, move):
        """
         Returns a new EightPuzzleState by applying the given move on the current
        board-state if it is valid. Otherwise, it throws Runtime Exception.

        :param move: A string ('up', 'down', 'left', 'right') represents the new location of the blank tile
        """
        blank_row, blank_col = self.blank_location
        if move == 'up':
            new_row = blank_row - 1
            new_col = blank_col
        elif move == 'down':
            new_row = blank_row + 1
            new_col = blank_col
        elif move == 'left':
            new_row = blank_row
            new_col = blank_col - 1
        elif move == 'right':
            new_row = blank_row
            new_col = blank_col + 1
        else:
            raise RuntimeError("Illegal Move")
        new_puzzle = EightPuzzleState()
        new_puzzle.board = [x[:] for x in self.board]
        new_puzzle.blank_location = new_row, new_col
        new_puzzle.board[new_row][new_col] = 0
        new_puzzle.board[blank_row][blank_col] = self.board[new_row][new_col]
        return new_puzzle

    def get_successor_moves(self):
        """
         Returns a list of strings ('up', 'down', 'left', 'right') representing the valid movements.
        """
        moves = []
        if self.blank_location[0] != 2:
            moves.append('down')
        if self.blank_location[0] != 0:
            moves.append('up')
        if self.blank_location[1] != 2:
            moves.append('right')
        if self.blank_location[1] != 0:
            moves.append('left')
        return moves # You have to check whether the returning array is empty or not in order to apply move.

    def print_board(self):
        for i in range(3):
            for j in range(3):
                sys.stdout.write('{} | '.format(self.board[i][j]))
            sys.stdout.write('\n')
        sys.stdout.flush()
        print('blank-tile location: {}, {}'.format(self.blank_location[0], self.blank_location[1]))

    def get_state_string(self):
        state_string = ""
        for i in range(3):
            for j in range(3):
                state_string += str(self.board[i][j])
                state_string += ","
        state_string = state_string[:-1]
        return state_string


def main():
    puzzle = EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8])
    puzzle.print_board()
    # print'Is goal state ? ', puzzle.is_goal()

    # moves = puzzle.get_successor_moves()

    # new_puzzle = puzzle.apply_move(moves[0])
    # new_puzzle.print_board()
    # print'Is goal state ? ', new_puzzle.is_goal()

    # new_puzzle = puzzle.apply_move(moves[1])
    # new_puzzle.print_board()
    # print'Is goal state ? ', new_puzzle.is_goal()

    # new_puzzle = puzzle.apply_move(moves[2])
    # new_puzzle.print_board()
    # print'Is goal state ? ', new_puzzle.is_goal()


if __name__ == '__main__':
    main()
