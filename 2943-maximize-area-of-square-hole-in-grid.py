class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars, vBars):
        # hbar_hash = set(hBars)
        # vbar_hash = set(vBars)

        # max_h = 1
        # count_h = 1
        # for i in range(1, n+2):
        #     if i + 1 in hbar_hash:
        #         count_h += 1
        #     else:
        #         max_h = max(max_h, count_h)
        #         count_h = 1
        
        # max_v = 1
        # count_v = 1
        # for i in range(1, m+2):
        #     if i + 1 in vbar_hash:
        #         count_v += 1
        #     else:
        #         max_v = max(max_v, count_v)
        #         count_v = 1

        hBars.sort()
        vBars.sort()

        max_h = 1
        cur_num = hBars[0]
        count_h = 2
        for i in range(1, len(hBars)):
            if hBars[i] == cur_num + 1 and hBars[i] < n + 2:
                count_h += 1
            else:
                max_h = max(max_h, count_h)
                count_h = 2
            cur_num = hBars[i]
        max_h = max(max_h, count_h)

        max_v = 1
        cur_num = vBars[0]
        count_v = 2
        for i in range(1, len(vBars)):
            if vBars[i] == cur_num + 1 and vBars[i] < m + 2:
                count_v += 1
            else:
                max_v = max(max_v, count_v)
                count_v = 2
            cur_num = vBars[i]
        max_v = max(max_v, count_v)

        return min(max_h, max_v) ** 2
    
s = Solution()
print(s.maximizeSquareHoleArea(n = 3, m = 2, hBars = [3, 2, 4], vBars = [3, 2]))