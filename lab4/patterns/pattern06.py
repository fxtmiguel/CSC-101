import driver


def letter(row, column):
    if column == row or column == (6 - row):
        return 'X'
    else:
        return 'O'


if __name__ == '__main__':
    driver.comparePatterns(letter)



