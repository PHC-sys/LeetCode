class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = sorted(list(set(nums)))
        
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]
        
        
        return len(new_nums)
        