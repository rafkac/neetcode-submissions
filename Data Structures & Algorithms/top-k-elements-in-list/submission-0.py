class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        # sort by values descending order
        sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse = True))

        return list(sorted_counts.keys())[:k]

        

        