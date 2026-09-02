class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        expected = set([i+1 for i in range(len(nums))])

        actual = set(nums)

        return list(expected - actual)

