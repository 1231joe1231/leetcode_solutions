# Sliding window
# Move right first until requirment not fulfilled, when this happened just move left
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def checkNoDup(s: str) -> bool:
            for x in range(len(s)):
                if s.count(s[x]) > 1:
                    return False
            return True

        if len(s) < 2:
            return len(s)
        else:
            left = 0
            right = 1
            longest = 0
            while right <= len(s) and left < right:
                substr = s[left:right]
                if checkNoDup(substr):
                    right += 1
                    if len(substr) > longest:
                        longest = len(substr)
                else:
                    left += 1
            return longest


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
