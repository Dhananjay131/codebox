class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        sz = len(nums1)
        tmp = nums1[:m] + nums2[:n]
        tmp.sort()
        
        for i in range(sz):
            if len(tmp) == i:
                break
            nums1[i] = tmp[i]
