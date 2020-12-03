import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    row_num = int(input('How many quick picks? '))
    while row_num < 0:
        print('invalid input')
        row_num = int(input('How many quick picks? '))
    for i in range(row_num):
        # this list contains random numbers for a row
        quick_picks = []
        for i in range(row_num):
            num = random.randint(MIN, MAX)
            while num in quick_picks:
                num = random.randint(MIN, MAX)
            quick_picks.append(num)
        quick_picks.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks))


main()
