import driver


def letter(row, column):
    if 1 < row < 5:
        if 2 < column < 7:
            return 'M'
    return 'S'


if __name__ == '__main__':
    driver.comparePatterns(letter)
