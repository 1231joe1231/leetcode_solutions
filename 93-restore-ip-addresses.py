class ListNode:
    def __init__(self, remain=0, parent=[], depth=0):
        self.remain = remain
        self.parent = parent
        self.depth = depth


class Solution:
    def __init__(self):
        self.addresses = []

    def format(self, list):
        s = ""
        for num in list:
            s += str(num) + "."
        return s[:-1]

    def getChild(self, node):
        if len(node.remain) == 0:
            # determine if every number is used
            if node.depth == 4:
                self.addresses.append(self.format(node.parent))
        else:
            if len(node.remain) >= 1:
                child = ListNode(
                    remain=node.remain[1:], parent=node.parent+[int(node.remain[0:1])], depth=node.depth+1)
                self.getChild(child)
            if len(node.remain) >= 2 and node.remain[0] != '0' and 0 <= int(node.remain[0:2]) < 256:
                child = ListNode(
                    remain=node.remain[2:], parent=node.parent+[int(node.remain[0:2])], depth=node.depth+1)
                self.getChild(child)
            if len(node.remain) >= 3 and node.remain[0] != '0' and 0 <= int(node.remain[0:3]) < 256:
                child = ListNode(
                    remain=node.remain[3:], parent=node.parent+[int(node.remain[0:3])], depth=node.depth+1)
                self.getChild(child)

    def restoreIpAddresses(self, s: str):
        root = ListNode(remain=s)
        self.getChild(root)
        print(self.addresses)
        self.addresses = []


s = Solution()
s.restoreIpAddresses("25525511135")
s.restoreIpAddresses("0000")
s.restoreIpAddresses("101023")
