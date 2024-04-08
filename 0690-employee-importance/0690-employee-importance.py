"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        def getImportancebyid(employees, id, sums=[]):
            for i in employees:
                if i.id == id:
                    sums.append(i.importance)
                    if len(i.subordinates)==0:
                        continue
                    for j in i.subordinates:
                        getImportancebyid(employees, j,sums)
            
        xx = [];
        getImportancebyid(employees, id, xx)
        return sum(xx)