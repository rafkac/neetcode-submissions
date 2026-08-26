class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            # shift to make it 0-indexed
            columnNumber -= 1

            remainder = columnNumber % 26

            result.append(chr(65 + remainder))

            columnNumber //= 26

        return "".join(result[::-1])


        