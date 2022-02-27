from typing import (
    List,
)

class Solution:
    """
    给定一个排序的整数数组（升序）和一个要查找的整数 target，
    用O(logn)O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。

    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def first_position(self, nums: List[int], target: int) -> int:
        # write your code here
        if (nums == None or len(nums) == 0):
            return -1
        left, mid, right = 0, 0, len(nums) - 1
        # get the first one that shows 
        # we need to update left with log(n)
        while (left < right):
            mid = left + (right - left)//2
            if (target > nums[mid]):
                left = mid + 1 
            else:  # target <= nums[mid]
                right = mid
        return left if (nums[left] == target) else -1
