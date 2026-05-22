class Solution:
    def findDisappearedNumbers(self, nums):
        nums_set = set(nums)
        n = len(nums)
        res = []
        for i in range(1, n + 1):
            if i not in nums_set:
                res.append(i)
        return res