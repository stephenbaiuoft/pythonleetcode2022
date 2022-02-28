from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Use the first element
        n = len(nums)        
        xor = n            
        for i in range(n):
            xor ^= (i ^ nums[i])

        return xor
        