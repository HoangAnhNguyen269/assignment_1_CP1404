"""
CP1404/CP5632 - Practical - Suggested Solution
Fixed program to determine score status
"""

# the score must be between 0 and 100 inclusive
# 90 or more is excellent; 50 or more is a pass
# below 50 is bad.
import random


def main():
    score = float(input("Enter score: "))
    print(mark_score(score))
    print('random score: ', end='')
    score = random.randint(0, 100)
    print(score)
    print(mark_score(score))


def mark_score(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == '__main__':
    main()
