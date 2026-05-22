class Solution:
    def prefixesDivBy5(self, nums):
        n = len(nums)
        res = []
        for i in range(n):
            num = 0
            for j in range(i+1):
                num += nums[j] * (2 ** (i - j))
            res.append(num % 5 == 0)
        return res

s = Solution()
print(s.prefixesDivBy5([0,1,1]))