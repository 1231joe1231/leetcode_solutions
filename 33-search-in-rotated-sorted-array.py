class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # left to mid is increasing
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # mid to right is increasing
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
print(s.search([4, 5, 6, 7, 0, 1, 2], 5))
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([3, 1], 0))
print(s.search([3, 1], 3))
print(s.search([1, 3], 1))
print(s.search([3, 5, 1], 5))
print(s.search([1, 3, 5], 1))
print(s.search([1, 3, 5], 5))
