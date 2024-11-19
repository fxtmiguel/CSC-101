import driver


def letter(row, column):
    if 3 < row < 6 and 6 < column < 10:
        return 'X'
    if 1 < row < 6 and 3 < column < 10:
        return 'Z'

    if 3 < row < 7 and 6 < column < 13:
        return 'B'

    return 'T'


if __name__ == '__main__':
    driver.comparePatterns(letter)
