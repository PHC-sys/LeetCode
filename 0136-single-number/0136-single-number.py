class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for num in nums:
            if not num in dic: dic[num]=1
            else: dic.pop(num)
        return list(dic.keys())[0]