from typing import List


class Solution:
    def __init__(self) -> None:
        pass
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        n = len(nums)
        for i in range(0, n - 2):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
                
            j = i + 1
            k = n - 1
            while (j < k):
                tot = nums[i] + nums[j] + nums[k]
                if (tot == 0):
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while( j < k and nums[j] == nums[j-1]):
                        j +=1
                    while (j < k and 
                           nums[k] == nums[k+1]):
                        k -= 1
                    # remove duplicates                        
                elif (tot > 0):
                    k -= 1
                else: # tot < 0
                    j+=1 
                    
        return result 


s = Solution()
s.threeSum([1,2,3,4,5])
                    
                    
