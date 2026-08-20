class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums.count(1)

        consecutives = [0]
        c = 1 if nums[0] == 1 else 0

        for i in range(1, len(nums)):
            match nums[i]:
                case 1:
                    c += 1
                    if i == len(nums) - 1:
                        consecutives.append(c)
                case _:
                    consecutives.append(c)
                    c = 0

        return max(consecutives)

        
        