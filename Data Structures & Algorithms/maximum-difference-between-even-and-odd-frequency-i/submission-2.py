class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = {}

        for char in s:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1

        vals = list(freqs.values())



        a1 = max(v for v in vals if v % 2 == 1)
        a2 = min(v for v in vals if v % 2 == 0)




        return a1-a2
        