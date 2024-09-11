#!/usr/bin/python3
"""N queens puzzle"""

import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def print_error_and_exit(message):
    print(message)
    sys.exit(1)

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col, solutions):
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1, solutions)
            board[i][col] = 0

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")
    
    if N < 4:
        print_error_and_exit("N must be at least 4")
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
