# Problem 31 - Coin sums
# ================================
# In England the currency is made up of pound, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, #1 (100p) and #2 (200p).
# It is possible to make #2 in the following way:
#
# How many different ways can #2 be made using any number of coins?


MONEY = [
    1,
    2,
    5,
    10,
    20,
    50,
    100,
    200
]

TARGET = 10


def main():
    a = set([tuple(sorted(a)) for a in findOptions(TARGET) if sum(a) == TARGET])
    return len(a)

def findOptions(target):
    a = [[]]
    for m in MONEY:
        if target < m:
            break
        else:
            for x in findOptions(target - m):
                a.append([m] + x)
    return a


if __name__ == "__main__":
    print main()
