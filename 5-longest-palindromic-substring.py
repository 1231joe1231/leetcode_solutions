class Solution:
    def longestPalindrome(self, s: str) -> str:
        matrix_length = len(s)+1
        longest = 1
        # for string without palindrome, use first char as answer
        left = 0
        right = 1
        dp = [[0] * matrix_length for _ in range(matrix_length)]
        # initialization every char is palindrome
        for i in range(matrix_length-1):
            dp[i][i + 1] = 1
        # IMPORTANT: we are getting answers from shorter string to longer string, therefore we need to iterate the string length
        for str_len in range(2, matrix_length):
            for i in range(matrix_length):
                j = i + str_len
                if j >= matrix_length:
                    break
                if str_len == 2 and s[i] == s[j - 1]:
                    dp[i][j] = 1
                elif dp[i + 1][j - 1] == 1 and s[i] == s[j - 1]:
                    dp[i][j] = 1
                # Update longest, left and right
                if dp[i][j] == 1 and j - i > longest:
                    longest = j - i
                    left = i
                    right = j
        return s[left:right]


s = Solution()
s.longestPalindrome("aacabdkacaa")
