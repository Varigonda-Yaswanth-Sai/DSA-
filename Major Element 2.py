"""
You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format.

Examples:

Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.
Input: arr[] = [1, 2, 3, 4, 5]
Output: []
Explanation: o candidate occur more than n/3 times.
Constraint:
1 <= arr.size() <= 106
-109 <= arr[i] <= 109

"""

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        if not arr:
            return []
        majority1=0
        majority2=0
        count1=0
        count2=0
        for num in arr:
            if num==majority1:
                count1+=1
            elif num==majority2:
                count2+=1
            elif count1==0:
                majority1=num
                count1+=1
            elif count2==0:
                majority2=num
                count2+=1
            else:
                count1-=1
                count2-=1
        
        count1,count2=0,0
        for num in arr:
            if num==majority1:
                count1+=1
            elif num==majority2:
                count2+=1
        res=[]
        if count1>len(arr)//3:
            res.append(majority1)
        if count2>len(arr)//3:
            res.append(majority2)
        return sorted(res)
        