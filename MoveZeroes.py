class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return 
        currentIndex = 0
        zeros_counter = 0
        for element in nums:
            if element != 0:
                nums[currentIndex] = element
                currentIndex += 1
            else: #if element == 0
                zeros_counter += 1
        if zeros_counter == 0:
            return
        else:
            nums[currentIndex:] = [0] * zeros_counter
            return
            
