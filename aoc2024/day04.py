import numpy as np

input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def count_occurrences(M, kernels):
    count = 0
    for kernel in kernels:
        kernel_mask = kernel != ""
        for i in range(M.shape[0] - kernel.shape[0] + 1):
            for j in range(M.shape[1] - kernel.shape[1] + 1):
                if np.all(
                    M[i : i + kernel.shape[0], j : j + kernel.shape[1]][kernel_mask]
                    == kernel[kernel_mask]
                ):
                    count += 1
    print(count)


M = np.array([list(row) for row in input.strip().split("\n")])

kernels_part1 = [
    np.array([["X", "M", "A", "S"]]),
    np.array([["S", "A", "M", "X"]]),
    np.array([["X"], ["M"], ["A"], ["S"]]),
    np.array([["S"], ["A"], ["M"], ["X"]]),
    np.array(
        [["X", "", "", ""], ["", "M", "", ""], ["", "", "A", ""], ["", "", "", "S"]]
    ),
    np.array(
        [["S", "", "", ""], ["", "A", "", ""], ["", "", "M", ""], ["", "", "", "X"]]
    ),
    np.array(
        [["", "", "", "X"], ["", "", "M", ""], ["", "A", "", ""], ["S", "", "", ""]]
    ),
    np.array(
        [["", "", "", "S"], ["", "", "A", ""], ["", "M", "", ""], ["X", "", "", ""]]
    ),
]

kernels_part2 = [
    np.array([["M", "", "M"], ["", "A", ""], ["S", "", "S"]]),
    np.array([["M", "", "S"], ["", "A", ""], ["M", "", "S"]]),
    np.array([["S", "", "M"], ["", "A", ""], ["S", "", "M"]]),
    np.array([["S", "", "S"], ["", "A", ""], ["M", "", "M"]]),
]

count_occurrences(M, kernels_part1)
count_occurrences(M, kernels_part2)
