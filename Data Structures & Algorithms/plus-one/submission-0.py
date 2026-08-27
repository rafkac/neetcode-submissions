class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        exp = 0

        if all(d == 9 for d in digits):
            return [1] + [0] * len(digits)

        for i in range(len(digits) -1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            elif digits[i] == 9:
                digits[i] = 0



        