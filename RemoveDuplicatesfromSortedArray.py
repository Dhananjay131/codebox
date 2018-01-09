from collections import OrderedDict
class Solution(object):
        """
        :type nums: List[int]
        :rtype: int
        """
        def removeDuplicates(self, nums):
            nums[:]=sorted(list(set(nums)))    # e.g., [1,1,2]-> [1,2]   nums gives [1,1], nums[:] giving [1,2]
            return len(nums)
