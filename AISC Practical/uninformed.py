count = 0

def nQueen(board, row, N):
    global count

    if row == N:
        count += 1
        print(f"Solution {count}:")

        for i in range(N):
            for j in range(N):
                if board[i] == j:
                    print('Q', end=" ")
                else:
                    print('-', end=" ")
            print()
        print()
        return

    for col in range(N):
        if possible(board, row, col, N):
            board[row] = col
            nQueen(board, row + 1, N)


def possible(board, row, col, N):
    for i in range(row):
        if (board[i] == col) or (abs(board[i] - col) == abs(i - row)):
            return False
    return True         


N = 4
board = [0 for _ in range(N)]

nQueen(board, 0, N)
