from typing import Optional
# https://leetcode.cn/problems/add-two-numbers/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode()
        head = res
        while l1 != None or l2 != None or carry != 0:
            res.next = ListNode()
            res = res.next
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            if carry >= 10:
                res.val = carry - 10
                carry = 1
            else:
                res.val = carry
                carry = 0
        return head.next
