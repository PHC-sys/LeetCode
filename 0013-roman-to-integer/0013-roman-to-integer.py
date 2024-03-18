class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        def converter(s):
            if s == 'I':
                return 1
            elif s == 'V':
                return 5
            elif s == 'X':
                return 10
            elif s == 'L':
                return 50
            elif s == 'C':
                return 100
            elif s == 'D':
                return 500
            elif s == 'M':
                return 1000

        def excp_converter(s):
            if s == 'IV':
                return 4
            elif s == 'IX':
                return 9
            elif s == 'XL':
                return 40
            elif s == 'XC':
                return 90
            elif s == 'CD':
                return 400
            elif s == 'CM':
                return 900
        
        
        exception = ['IV', 'IX', 'XL', 'XC','CD','CM']
        result = 0

        # 2개씩 잘라서 읽고
        # 예외 사항에 없으면 앞 글자 > 숫자
        # 예외 사항에 있으면 두 글자 > 숫자
        n = 0
        for i in range(len(s)):
            if n >= len(s):
                break

            two_str = s[n:n+2]
            if two_str not in exception:
                result += converter(two_str[0])
                n += 1

            elif two_str in exception:
                result += excp_converter(two_str)
                n += 2
                
        return result