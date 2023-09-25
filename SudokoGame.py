import numpy as np
from time import time

table = [
    [], [], [], [], [], [], [], [], []
]


def fill_array(lst: list):
    current_index = 0

    for i in range(9):
        for _ in range(9):
            lst[i].append(initial_table[current_index])
            current_index += 1


def show_table(table):
    for i in range(len(table)):
        print(table[i])


def square_nighbors(index, t=table):
    lst = []
    i_square_start = int(index[0] - (index[0] % 3))
    j_square_start = int(index[1] - (index[1] % 3))
    for row in range(i_square_start, i_square_start + 3):
        for col in range(j_square_start, j_square_start + 3):
            if row != index[0] or col != index[1]:
                lst.append(t[row][col])
    return lst


def is_valid(index, number, t=table):
    #           checking row                        checking column                         checking square
    if number not in table[index[0], :] and number not in table[:, index[1]] and number not in square_nighbors(index,table):
        return True
    return False


solution_sequence = []


def solve_sudoku(t):
    for row in range(9):
        for col in range(9):
            if t[row][col] == '0':
                for num in range(1, 10):
                    if is_valid((row, col), str(num), t):
                        t[row][col] = str(num)

                        if solve_sudoku(t):
                            return True
                        else:
                            t[row][col] = "0"
                return False
    return True


initial_table = input("insert the initial table:")
fill_array(table)

table = np.array(table)
start = time()
solve_sudoku(table)
end = time()

# print(square_nighbors((4,1),table))
# 070000043040009610800634900094052000358460020000800530080070091902100005007040802


show_table(table)

actual_sol = "679518243543729618821634957794352186358461729216897534485276391962183475137945862"

print("elapsed time: ", (end - start))
