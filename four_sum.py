"""
Given an array arr[] of integers and another integer target. Find all unique quadruples from the given array that sums up to target.

Note: All the quadruples should be internally sorted, ie for any quadruple [q1, q2, q3, q4] it should be : q1 <= q2 <= q3 <= q4.

Examples :

Input: arr[] = [0, 0, 2, 1, 1], target = 3
Output: [0, 0, 1, 2] 
Explanation: Sum of 0, 0, 1, 2 is equal to 3.
Input: arr[] = [10, 2, 3, 4, 5, 7, 8], target = 23
Output: [[2, 3, 8, 10], [2, 4, 7, 10], [3, 5, 7, 8]] 
Explanation: Sum of 2, 3, 8, 10 is 23, sum of 2, 4, 7, 10 is 23 and sum of 3, 5, 7, 8 is also 23.
Input: arr[] = [0, 0, 2, 1, 1], target = 2
Output: [0, 0, 1, 1] 
Explanation: Sum of 0, 0, 1, 1 is equal to 2.
Constraints:
1 <= arr.size() <= 200
-106 <= target <= 106
-106 <= arr[i] <= 106

"""
#User function Template for python3

# arr[] : int input array of integers
# target : the quadruple sum required
class Solution:
    def fourSum(self, arr, target):
        # code here
        n=len(arr)
        arr.sort()
        res=[]
        for i in range(0,n):
            if i>0 and arr[i]==arr[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and arr[j]==arr[j-1]:
                    continue
                left=j+1
                right=n-1
                while left<right:
                    total=arr[i]+arr[j]+arr[left]+arr[right]
                    if total==target:
                        res.append([arr[i],arr[j],arr[left],arr[right]])
                        left+=1
                        right-=1
                        while left<right and arr[left]==arr[left-1]:
                            left+=1
                        while left<right and arr[right]==arr[right+1]:
                            right-=1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        return res
arr=[0, 0, 2, 1, 1]
target=0 
sol=Solution()
print(sol.fourSum(arr,target))