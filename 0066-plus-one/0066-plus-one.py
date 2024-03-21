class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n = 0
        for i in range(len(digits)):
            n += digits[i]*10**(len(digits)-i-1)

        n+=1
        
        n_list = [int(x) for x in str(n)]
        
        return n_list