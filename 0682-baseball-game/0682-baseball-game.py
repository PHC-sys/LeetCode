class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        :type operations: List[str]
        :rtype: int
        """
        vaild = [];
        
        s = 0;
        for i in operations:
            if re.match('^-*[0-9]+$',i) :
                s = s + int(i);
                vaild.append( int(i) );
            if i == 'C':
                s = s - vaild[len(vaild)-1];
                vaild.pop();
            if i == 'D':
                s = s + vaild[len(vaild)-1]*2;
                vaild.append(vaild[len(vaild)-1]*2);
            if i == '+':
                s = s + vaild[len(vaild)-1] + vaild[len(vaild)-2]
                vaild.append(vaild[len(vaild)-1] + vaild[len(vaild)-2])
        return s