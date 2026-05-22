class Solution:
    def plusOne(self, digits):
        carry = 1
        result = []
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i] + carry
            if digit == 10:
                digit = 0
                carry = 1
            else:
                carry = 0
            result.insert(0, digit)
        if carry == 1:
            result.insert(0, carry)
        return result
    
s = Solution()
print(s.plusOne(digits=[9]))