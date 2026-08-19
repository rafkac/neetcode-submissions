class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for char in reversed(s):
            if char == " " and length > 0:
                return length
            if char != " ":
                length += 1
            
        return length
            
        