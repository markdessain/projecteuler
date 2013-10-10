# Problem 36 - Double-base palindromes
# ================================
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)


def main():
    total = 0
    
    for i in range(1000000):
        reverseDecimal = list(str(i))
        reverseDecimal.reverse()

        if list(str(i)) == reverseDecimal:
            binaryString = str(bin(i))[2:]
            reverseBinary = list(binaryString)
            reverseBinary.reverse()
            if list(binaryString) == reverseBinary:
                total += i

    return total


if __name__ == "__main__":
    print main()

