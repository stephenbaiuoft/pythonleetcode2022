class Solution:
    def countSubstrings(self, s: str) -> int:
        # 2-d array
        n = len(s)
        # how to init 2-d array
        dp = [[False for i in range(n)] for _ in range(n)]
        # dp[i][j] = (dp[i+1][j-1] && s[i] == s[j]) or (i == j-1) or (i==j)
        sum = 0
        # start n-1, decrease -1, and stop before -1
        for i in range(n-1, -1, -1):
            j = i
            while (j < n):
                dp[i][j] = (s[i] == s[j]) and (j - i <= 2 or dp[i+1][j-1])            
                if (dp[i][j]):
                    sum += 1                
                j+=1

                    
        return sum 

s = Solution()
s.countSubstrings("abc")