def get_heuristic_cost(gameState, heuristic='manhattan'):
    cost = 0
    board = gameState.board
    for i in range(3):
        for j in range(3):
            cost = cost + get_heuristic_distance(board[i][j] ,i , j, heuristic)
    return cost



def get_heuristic_distance (value, i, j, heuristic):
        originalI = int(value / 3)
        originalJ = value % 3
        distance = 0
        if heuristic == 'manhattan':
            distance = (abs(originalI - i) + abs(originalJ - j))
        elif heuristic == 'euclidean':
            distance = sqrt((originalI - i)**2 + (originalJ - j)**2)
        return distance

def main():
    print(get_heuristic_distance(5, 2, 1, "manhattan"))

if __name__ == '__main__':
    main()