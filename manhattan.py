def main():
    # Test: Lista de listas para x e y
    x: list = [[-1, 1, 3, 2], [2, 1], [1]]
    y: list = [[5, 6, 5, 3], [1,3], [2]]

    if not valid_input(x, y):
        print("The input is not valid")
        return

    x_len: int = len(x)
    for i in range(x_len):
        if not valid_input(x[i], y[i]):
            print("The input is not valid")
            return
        size: int = len(x[i])
        print(f'Total: {manhattan(x[i], y[i], size)}')


def valid_input(x: list, y: list):
    len_x: int = len(x)
    len_y: int = len(y)
    return 2 <= len_x and 2 <= len_y and len_x == len_y

def manhattan(x: list, y: list, n: int):
    acum: int = 0
    for i in range(n):
        for j in range(i + 1, n):
            acum += manhattan_distance(x[i], y[i], x[j], y[j])
    return acum


def manhattan_distance(x1: int, y1: int, x2: int, y2: int):
    return abs(x1 - x2) + abs(y1 - y2)

"""
if __name__ == '__main__':
    main()
"""