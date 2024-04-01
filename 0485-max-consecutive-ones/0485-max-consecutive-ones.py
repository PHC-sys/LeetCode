class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        str_nums = ''.join([str(i) for i in nums]);
        splited_nums = str_nums.split('0')
        return max([len(i) for i in splited_nums ])