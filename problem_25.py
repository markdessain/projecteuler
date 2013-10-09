# Problem 25 - 1000-digit Fibonacci number
# ================================
# The Fibonacci sequence is defined by the recurrence relation:
#

# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?


MAX_NUMBER = 10**(1000 - 1)


def main():
    a = 1
    b = 1
    c = a + b
    i = 2
    while c < MAX_NUMBER:
        c = a + b
        a = b
        b = c
        i += 1
    return i


if __name__ == "__main__":
    print main()


