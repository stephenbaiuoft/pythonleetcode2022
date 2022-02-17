from ast import List

# https://leetcode.com/problems/missing-element-in-sorted-array/
"""
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k,
return the kth missing number starting from the leftmost number of the array.

需要log（n）
"""

"""
思路 
- sorted array 
- 第二 logn 大概率是 binary search
 - 好 那binary search需要什么？ 需要一个计算 computation that determines whether we go left or right
 - define missing(idx), that computes # of missing from idx= 0 

- missing(idx) < k <=missing(idx+1) 
 - value = nums[idx] + k - missing(idx) 

- define a method that tells you # of missing for a given idx, missing(idx) from idx = 0!!!! 
 - idx 到 0 miss 多少
  - 0 to idx 就是有idx这么多个数 （不包括0)

nums:   [4, 6, 7]
idices: [0, 1, 2] 

missing = nums[idx] - nums[0] - idx 


missing(indx)
"""


class Solution:
    # This is log(n)
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = lambda idx: nums[idx] - nums[0] - idx
        n = len(nums)
        if missing(n - 1) < k:
            return nums[n - 1] + k - missing(n - 1)
        
        left = 0; right = n-1; mid = 0
        #  binarysearch
        while (left < right - 1):
            mid = left + (right - left)//2
            if (missing(mid) < k):
                left = mid
            else: # missing(mid) >= k
                right = mid 
        # left = right - 1
        return nums[left] + k - missing(left)
 


    def _missingElement(self, nums: List[int], k: int) -> int:
        missing = lambda idx: nums[idx] - nums[0] - idx

        n = len(nums)
        # if Kth missing number is larger than the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        idx = 1
        # find idx s.t. missing (idx -1) < k <= missing(idx)

        while (missing(idx)) < k:
            idx += 1

        # kth missing number if greater than nums[idx-1]
        # and less than nums[idx]
        # it's idx -1
        return nums[idx - 1] + k - missing(idx - 1)
