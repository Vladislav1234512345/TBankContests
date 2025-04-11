import sys

def count_finish_chess_board_with_horse(height: int, width: int) -> int:
    chess_board = [[0] * width for _ in range(height)]
    chess_board[0][0] = 1

    reversed_steps = [(-2, -1), (-1, -2), (-2, 1), (1, -2)]
    for i in range(height):
        cur_i = i
        j = 0
        while cur_i >= 0 and j < width:
            for reversed_step in reversed_steps:
                if 0 <= cur_i + reversed_step[0] < height and 0 <= j + reversed_step[1] < width:
                    chess_board[cur_i][j] += chess_board[cur_i + reversed_step[0]][j + reversed_step[1]]
            cur_i -= 1
            j += 1

    for j in range(1, width):
        i = height - 1
        cur_j = j
        while i >= 0 and cur_j < width:
            for reversed_step in reversed_steps:
                if 0 <= i + reversed_step[0] < height and 0 <= cur_j + reversed_step[1] < width:
                    chess_board[i][cur_j] += chess_board[i + reversed_step[0]][cur_j + reversed_step[1]]
            i -= 1
            cur_j += 1

    return chess_board[height - 1][width - 1]

n, m = map(int, sys.stdin.readline().split())

print(count_finish_chess_board_with_horse(height=n, width=m))

