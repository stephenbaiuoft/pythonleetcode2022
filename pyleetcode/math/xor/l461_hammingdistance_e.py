class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        
        count = 0
        # need to count # of 1 ones
        # 1, 0, 1, 1
        # if %2, this means the last bit is 1
        while (xor > 0):
            if (xor % 2 == 1):
                count += 1
            xor = xor >> 1
        
        return count 
        
        