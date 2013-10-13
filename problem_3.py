# Problem 3 - Largest prime factor
# ================================
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def main():

    target = 600851475143
    largestFactor = 0
    i = 2

    while i * i < target:
        if target % i == 0:
            target = target / i
            largestFactor = i
        else:
            i += 1

    return largestFactor if largestFactor > target else target


if __name__ == "__main__":
    print main()
