"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

"""

from typing import List
class Solution:
    def generaterow(self,row: int) -> List[int]:
        ans=1
        ans_row=[1]
        for i in range(1,row):
            ans=ans*(row-i)
            ans=ans//i
            ans_row.append(ans)    
        return ans_row
    
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(1,numRows+1):
            res.append(self.generaterow(i))
        return res