"""
Given an array arr containing both positive and negative integers, the task is to compute the length of the largest subarray that has a sum of 0.

Examples:

Input: arr[] = [15, -2, 2, -8, 1, 7, 10, 23]
Output: 5
Explanation: The largest subarray with a sum of 0 is [-2, 2, -8, 1, 7].
Input: arr[] = [2, 10, 4]
Output: 0
Explanation: There is no subarray with a sum of 0.
Input: arr[] = [1, 0, -4, 3, 1, 0]
Output: 5
Explanation: The subarray is [0, -4, 3, 1, 0].
Constraints:
1 ≤ arr.size() ≤ 106
−103 ≤ arr[i] ≤ 103, for each valid i

"""
#Your task is to complete this function
 
class Solution:
    def maxLen(self, arr):
        # code here
        n=len(arr)
        hashmap={}
        count=0
        Sum=0
        max_len=0
        for i in range(0,n):
            Sum+=arr[i]
            if Sum==0:
                max_len=i+1
            else:
                if Sum in hashmap:
                    max_len=max(max_len,i-hashmap[Sum])
                else:
                    hashmap[Sum]=i
        return max_len
                