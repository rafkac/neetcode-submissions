class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i, _ in enumerate(s[:-1]):
            score += abs(ord(s[i]) - ord(s[i+1]))
        return score