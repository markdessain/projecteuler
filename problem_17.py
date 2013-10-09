# Problem 17 - Number letter counts
# ================================
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance
# with British usage.


import unittest


BELOW_20 = [
    None,
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]
TENS = [
    None,
    None,
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]
HUNDRED = 'hundred'
THOUSAND = 'thousand'
NUMBER_TEN = 10
NUMBER_HUNRED = 100
NUMBER_THOUSAND = 1000


def numberToWord(number):
    parts = []

    parts.append(BELOW_20[number / NUMBER_THOUSAND])
    parts.append(THOUSAND if number / NUMBER_THOUSAND else None)
    number = number % NUMBER_THOUSAND

    parts.append(BELOW_20[number / NUMBER_HUNRED])
    parts.append(HUNDRED if number / NUMBER_HUNRED else None)
    number = number % NUMBER_HUNRED

    if number < len(BELOW_20):
        parts.append(BELOW_20[number])
    else:
        parts.append(TENS[number / NUMBER_TEN])
        number = number % NUMBER_TEN
        parts.append(BELOW_20[number])

    try:
        parts = [p for p in parts if p]
        if len(parts) > parts.index(HUNDRED) + 1:
            parts.append('and')
    except ValueError:
        pass

    return parts


def countLetters(wordList):
    return len([j for i in wordList for j in i])


class TestSequenceFunctions(unittest.TestCase):

    def testTeenAndBelow(self):
        self.assertEqual(numberToWord(15), ['fifteen'])

    def testDoubleDigit(self):
        self.assertEqual(numberToWord(47), ['forty', 'seven'])

    def testHunderedDigit(self):
        self.assertEqual(numberToWord(115), ['one', 'hundred', 'fifteen', 'and'])

    def testHunderedDigitTwo(self):
        self.assertEqual(numberToWord(342), ['three', 'hundred', 'forty', 'two', 'and'])

    def testThousandDigitThree(self):
        self.assertEqual(numberToWord(100), ['one', 'hundred'])

    def testThousandDigit(self):
        self.assertEqual(numberToWord(1000), ['one', 'thousand'])

    def testCountLists(self):
        self.assertEqual(countLetters(['one', 'thousand']), 11)


def main():
    return sum([countLetters(numberToWord(i)) for i in range(1, 1001)])


if __name__ == "__main__":
    unittest.main()
    #print main()


