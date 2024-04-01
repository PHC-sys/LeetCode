class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        :type n: int
        :rtype: List[str]
        """
        re = [];
        for i in range(1,n+1):
            if i % 3 ==0 and i % 5==0:
                re.append("FizzBuzz")
            elif i % 5 == 0:
                re.append("Buzz")
            elif i % 3 == 0:
                re.append("Fizz")
            else:
                re.append(str(i))
                
        return re