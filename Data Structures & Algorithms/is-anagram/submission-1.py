class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars1 = list(s)
        chars2 = list(t)
        chars1.sort()
        chars2.sort()
        return chars1 == chars2
        