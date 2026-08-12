class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        treshold = len(nums) / 2

        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
                
            if d[n] > treshold:
                    return n

            
        