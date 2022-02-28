class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        answer = [0] * (n+1)
        
        # reverse
        a = a[::-1]
        b = b[::-1]
        
        # 0 to n inclusive
        for i in range(n+1):
            tot = answer[i]
            if (i < len(a)):
                tot += int(a[i])
            if (i < len(b)):
                tot += int(b[i])
            # carry over if necessary
            if (tot >= 2):
                answer[i+1] = tot // 2
                answer[i] = tot %2
            else: # not carrying over
                answer[i] = tot
            answer[i] = tot
                
        if (answer[n] == 0):
            answer.pop()
        
        return "".join([str(d) for d in reversed(answer)])
        
s = Solution()
s.addBinary("1010", "1011")