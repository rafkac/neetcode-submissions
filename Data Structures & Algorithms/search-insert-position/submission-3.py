class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            middle = (l+r) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:     # go higer
                l = middle + 1
            else:                           # go higher
                r = middle - 1

        return l