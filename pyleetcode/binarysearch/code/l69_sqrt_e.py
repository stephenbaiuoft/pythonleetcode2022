class Solution:
    # 2分法 -> 就用模版来做
    ## left < right - 1
    ### 意味着需要check而已


    def mySqrt(self, x: int) -> int:
        # 0, 1 always going to be itself
        if (x < 2):
            return x 
        
        left, mid, right = 0, 0, x
        # let's always search the mid endpoint
        # note we need to take smaller chunk
        while (left < right - 1):
            mid = left + (right - left)//2
            
            div = x // mid
            # div is larger than mid 
            # 9/2 = 4, 4 > 2, then start 
            if (div > mid):
                left = mid
            else: # div <= mid 
                right = mid
        
        return left if right * right > x else right
            