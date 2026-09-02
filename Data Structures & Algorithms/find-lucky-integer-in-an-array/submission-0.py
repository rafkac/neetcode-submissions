from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:

        counts = {}

        for x in arr:
            counts[x] = counts.get(x, 0) + 1

        largest = -1
        for key, value in counts.items():
            if key == value:
                largest = max(largest, key)
        return largest
        