class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        visited = [0] * n
        dup = n
        for i in nums:
            if visited[i - 1] != 0:
                dup = i
            else:
                visited[i - 1] = 1
        missing = visited.index(0) + 1
        return [dup, missing]
            
s = Solution()
s.findErrorNums([1,2,2,4])