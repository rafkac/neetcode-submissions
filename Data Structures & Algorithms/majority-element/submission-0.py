class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()

        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1

        # sort descending by values
        sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))


        first_key = next(iter(sorted_d))
        return first_key

        