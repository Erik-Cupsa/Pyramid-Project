def read_pyramid(file_path):
    pyramid = []
    with open(file_path, 'r') as file:
        target = int(file.readline().strip().split(": ")[1])
        for line in file:
            row = list(map(int, line.strip().split(',')))
            pyramid.append(row)
    return pyramid, target

def find_path(pyramid, target, row=0, col=0, path=""):
    if row == len(pyramid) - 1:
        if pyramid[row][col] == target:
            print("Solution path:", path)
        return

    find_path(pyramid, target / pyramid[row][col], row + 1, col, path + "L")
    find_path(pyramid, target / pyramid[row][col], row + 1, col + 1, path + "R")

pyramid, target = read_pyramid("pyramid_sample_input.txt")

find_path(pyramid, target)
