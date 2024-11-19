import driver


def letter(row, column):
    if row == 9 and column == 9:
        return 'Z'
    else:
        return 'G'


if __name__ == '__main__':
    driver.comparePatterns(letter)
