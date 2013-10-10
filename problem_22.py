# Problem 22 - Names scores
# ================================
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
# first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 x  53 = 49714.
#
# What is the total of all the name scores in the file?


import string
import unittest


CHARACTERS = string.lowercase[:26]


def loadFile(file):
    with open(file, 'r') as f:
        names = f.next().replace('"', '').split(',')
    return sorted(names)


def countCharacters(names):
    return sum(
        sum(
            CHARACTERS.index(character) + 1
            for character in name.lower()
        ) * (i + 1)
        for i, name in enumerate(names)
    )


class TestProblem22(unittest.TestCase):

    def testCountCharactersSingleName(self):
        self.assertEqual(countCharacters(['abcxyz']), 81)

    def testCountCharactersMultipleName(self):
        self.assertEqual(countCharacters(['abc', 'abc']), 18)

    def testSorting(self):
        names = loadFile('problem_22_names.txt')
        self.assertEqual(names.index('COLIN'), 937)

    def testProblem(self):
        names = loadFile('problem_22_names.txt')
        print countCharacters(names)


if __name__ == "__main__":
    unittest.main()



