class Solution:
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        sorted_nums = nums[:]
        sorted_nums.sort()
        sorted_index = {}
        res = [0] * n
        for i in range(n):
            num = sorted_nums[i]
            if num not in sorted_index:
                sorted_index[num] = i
        for i in range(n):
            num = nums[i]
            res[i] = sorted_index[num]
        return res

s = Solution()
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))