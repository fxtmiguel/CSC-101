import driver


def letter(row, column):
    if column > (row - 1):
        return 'W'
    else:
        return 'T'


if __name__ == '__main__':
    driver.comparePatterns(letter)