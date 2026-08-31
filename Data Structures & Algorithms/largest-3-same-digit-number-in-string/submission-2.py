class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums = []
        for i in range(len(num) - 2):
            n = num[i:i+3]
            if n[0] == n[1] == n[2]:
                nums.append(n)

        if nums:
            return (max(nums))
        else:
            return ""
