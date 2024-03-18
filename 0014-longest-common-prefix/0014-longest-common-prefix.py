class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        not_in_sign = False

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    not_in_sign = True
                    break
                
                else:
                    if strs[0][i] != strs[j][i]:
                        not_in_sign = True
                        break
                    
            if not_in_sign:
                break

            else:    
                prefix += strs[0][i]
        
        return prefix