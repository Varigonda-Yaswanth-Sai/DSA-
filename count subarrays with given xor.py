"""
Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.

Examples: 

Input: arr[] = [4, 2, 2, 6, 4], k = 6
Output: 4
Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.
Input: arr[] = [5, 6, 7, 8, 9], k = 5
Output: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]. Hence, the answer is 2.
Input: arr[] = [1, 1, 1, 1], k = 0
Output: 4
Explanation: The subarrays are [1, 1], [1, 1], [1, 1] and [1, 1, 1, 1].
Constraints:

1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤105
0 ≤ k ≤ 105


"""
from collections import defaultdict
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        n=len(arr)
        xor=0
        mpp=defaultdict(int)
        mpp[0]=1
        count=0
        for i in range(0,n):
            xor^=arr[i]
            x=xor^k
            count+=mpp[x]
            mpp[xor]+=1
        return count
arr = [4, 2, 2, 6, 4]
k = 6
sol=Solution()
print(sol.subarrayXor(arr,k))
