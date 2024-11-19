import driver


def letter(row, column):
    if column > 9:
        return 'O'
    else:
        return 'X'


if __name__ == '__main__':
    driver.comparePatterns(letter)
