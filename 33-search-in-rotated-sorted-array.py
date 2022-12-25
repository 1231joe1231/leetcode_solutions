class Solution:
    def search(self, nums, target: int) -> int:
        # First find the index of rotation, must be the index of minimum
        left = 0
        right = len(nums) - 1
        while right > left:
            mid = (left+right) // 2
            if nums[right] < nums[mid]:
                right = mid
            else:
                left = mid
        # mid is the rotation index
        rotation_index = right
        nums = nums[rotation_index:len(nums)] + nums[:rotation_index]
        # now search for target
        left = 0
        right = len(nums) - 1
        rotated_target = -1
        while right >= left:
            mid = (left+right) // 2
            if target == nums[mid]:
                rotated_target = mid
                break
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        if rotated_target == -1:
            return -1
        else:
            tmp = rotated_target + rotation_index
            if tmp > len(nums):
                return tmp - len(nums)
            else:
                return tmp


s = Solution()
# print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
# print(s.search([4, 5, 6, 7, 0, 1, 2], 5))
# print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([3, 1], 0))
print(s.search([1, 3], 1))
