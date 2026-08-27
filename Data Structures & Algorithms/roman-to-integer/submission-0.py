class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0

        for i, letter in enumerate(s[:-1]):
            if roman[s[i+1]] > roman[letter]:
                number -= roman[letter]
            else:
                number += roman[letter]

        return number + roman[s[-1]]


        