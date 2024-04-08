class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic=dict()
        for num in nums:
            if not num in dic:
                dic[num]=1
            else:
                return True
        return False