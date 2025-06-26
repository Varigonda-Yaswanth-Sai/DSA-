"""
Given an integer array arr, return all the unique triplets [arr[i], arr[j], arr[k]] such that i != j, i != k, and j != k, and arr[i] + arr[j] + arr[k] == 0.

Note: The triplets must be returned in sorted order, the solution vector should also be sorted, and the answer must not contain any duplicate triplets.

Examples:

Input: arr = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: arr[0] + arr[1] + arr[2] = (-1) + 0 + 1 = 0.
arr[1] + arr[2] + arr[4] = 0 + 1 + (-1) = 0.
arr[0] + arr[3] + arr[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Input: arr = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(n2)

Constraints:
3 <= arr.length <= 3000
-105 <= arr[i] <= 105

"""
class Solution:
    def triplets(self, arr ):
        # code here
        n=len(arr)
        arr.sort()
        res=[]
        for i in range(0,n):
            if i>0 and arr[i]==arr[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total=arr[i]+arr[j]+arr[k]
                if total<0:
                    j+=1
                elif total>0:
                    k-=1
                else:
                    res.append([arr[i],arr[j],arr[k]])
                    j+=1
                    k-=1
                    while j<k and arr[j]==arr[j-1]:
                        j+=1
                    while j<k and arr[k]==arr[k+1]:
                        k-=1
        return res