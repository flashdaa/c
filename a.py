from queue import PriorityQueue
import numpy as np

def solve_puzzle(initial, goal):
    def find_zero(state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def get_moves(state):
        x, y = find_zero(state)
        moves = []
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                moves.append(new_state)
        return moves

    def heuristic(state):
        return sum(state[i][j] != goal[i][j] for i in range(3) for j in range(3))

    queue = PriorityQueue()
    queue.put((0, initial, []))
    visited = set()

    while not queue.empty():
        _, current, path = queue.get()
        if current == goal:
            return path + [current]
        visited.add(str(current))
        for move in get_moves(current):
            if str(move) not in visited:
                queue.put((heuristic(move), move, path + [current]))

    return None

initial = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
solution = solve_puzzle(initial, goal)

if solution:
    print(f"Solution in {len(solution) - 1} moves:")
    for state in solution:
        for row in state:
            print(row)
        print()
