class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for w in words:
            if all(c in allowed for c in w):
                res += 1

        return res
