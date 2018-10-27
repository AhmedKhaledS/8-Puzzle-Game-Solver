from math import sqrt


def get_heuristic_cost(gameState, heuristic='manhattan'):
    """
    Computes a heuristic cost for the input game state.
    :param gameState: game state for which heuristic cost is computed
    :param heuristic: the heuristic formula to be used.
    :return: int heuristc cost
    """
    cost = 0
    board = gameState.board
    for i in range(3):
        for j in range(3):
            cost = cost + get_heuristic_distance(board[i][j], i, j, heuristic)
    return cost



def get_heuristic_distance (value, i, j, heuristic):
    """
    Computes a heuristic distance for a single element.
    :param value: value of cell
    :param i: value's row index.
    :param j: value's column index
    :param heuristc: heuristc formula to be used
    :return: int heuristc distance
    """
    originalI = int(value / 3)
    originalJ = value % 3
    distance = 0
    if heuristic == 'manhattan':
        distance = (abs(originalI - i) + abs(originalJ - j))
    elif heuristic == 'euclidean':
        distance = sqrt((originalI - i)**2 + (originalJ - j)**2)
        print(distance)
    return distance

def main():
    print(get_heuristic_distance(5, 2, 1, "euclidean"))

if __name__ == '__main__':
    main()
