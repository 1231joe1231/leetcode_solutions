class Solution:
    def minRemoval(self, nums, k: int):
        if len(nums) == 1:
            return 0
        nums.sort()
        n = len(nums)
        min = n
        j = 0
        for i in range(n):
            while j < n and nums[j] <= nums[i] * k:
                j += 1
            cur_remove = n - (j - i)
            if cur_remove < min:
                min = cur_remove
        return min
    
s = Solution()
print(s.minRemoval(nums = [2,12], k = 2))