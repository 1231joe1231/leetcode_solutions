# prefix sum
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        prefix_hash = {0: 1}
        prefix = 0
        count = 0
        for n in nums:
            prefix += n
            if prefix - k in prefix_hash:
                count += prefix_hash[prefix - k]
            if prefix in prefix_hash:
                prefix_hash[prefix] += 1
            else:
                prefix_hash[prefix] = 1
        return count


s = Solution()
print(s.subarraySum([1, 2, -3], 0))
