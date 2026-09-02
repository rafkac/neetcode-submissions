class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = [], [], []

        for n in nums:
            if n == 0:
                zeros.append(n)
            elif n == 1:
                ones.append(n)
            else:
                twos.append(n)

        nums[:] = zeros + ones + twos