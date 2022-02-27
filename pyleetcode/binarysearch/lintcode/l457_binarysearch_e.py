class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here
        if nums == None or len(nums) == 0:
            return -1

        left, mid, right = 0, 0, len(nums) - 1
        # binary search
        while left < right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            else:  # target <= nums[mid]
                right = mid

        return -1 if (nums[left] != target) else left
