class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        sumx = 0
        # get the results of
        nums.sort();
        for i,v in enumerate(nums):
            if i%2 == 0:
                sumx = sumx + v;
                
        return sumx;
     