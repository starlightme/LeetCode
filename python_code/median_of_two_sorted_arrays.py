class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new_num = nums1 + nums2
        new_num.sort()
        if len(new_num) %2 != 0:
            return new_num[len(new_num)/2]
        else:
            return (new_num[len(new_num)/2] + new_num[len(new_num)/2-1]) /2.0
