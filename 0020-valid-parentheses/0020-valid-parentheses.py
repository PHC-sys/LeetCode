class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        new_code = s

        while True:
            print('New iteration')
            s = new_code    
            for i in range(len(s)):
                if i > len(s):
                    break
                sign = s[i:i+2]

                if sign == '()' or sign == '[]' or sign == '{}':
                    new_code = s.replace(s[i:i+2], '')
                    break

            if new_code == s:
                break

        if s == '':
            return True
        else:
            return False