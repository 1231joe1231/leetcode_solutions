class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = []
        for i in nums:
            if i != 0:
                non_zero.append(i)
        nums = non_zero + ([0] * (len(nums) - len(non_zero)))
        print(nums)

s = Solution()
s.moveZeroes([0,1,0,3,12])