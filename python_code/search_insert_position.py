class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in xrange( len(nums) ):
            cmp_num = nums[i]
            if target <= cmp_num:
                return i
        return i + 1