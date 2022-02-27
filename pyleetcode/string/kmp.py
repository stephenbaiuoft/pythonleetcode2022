from typing import List
from black import main


class KMP:
    # kmp algorithm
    def match(self, s: str, p: str) -> List[int]:
        # compare prefix with index = 0, and prefix with index 1
        def buildNxt(prefix: str) -> List[int]:
            m = len(prefix)
            nxt = [0, 0]
            j = 0
            for i in range(1, m):
                while j > 0 and prefix[i] != prefix[j]:
                    j = nxt[j]
                if prefix[i] == prefix[j]:
                    j += 1
                nxt.append(j)
            return nxt

        n, m = len(s), len(p)
        nxt = buildNxt(p)
        ans = []
        # j is p starting index
        j = 0
        # 0 to n - 1
        for i in range(n):
            # always check iterate on j
            while j > 0 and s[i] != p[j]:
                j = nxt[j]
            # always check if j can be incremented by 1
            if s[i] == p[j]:
                j += 1
            # if j has reached m, meaning a perfect match
            if j == m:
                ans.append(i - m + +1)
                j = nxt[j]

        return ans
