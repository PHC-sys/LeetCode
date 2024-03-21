class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new_nums = [i for i in nums if i is not val]
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]
        
        return len(new_nums)