# Problem 16 - Power digit sum
# ================================
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?


import math


def main():
    return sum(int(x) for x in str(int(math.pow(2, 1000))))


if __name__ == "__main__":
    print main()
