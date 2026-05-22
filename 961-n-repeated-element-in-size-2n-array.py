class Solution:
    def repeatedNTimes(self, nums):
        frequency = {}
        for num in nums:
            if num in frequency:
                return num
            else:
                frequency[num] = 1