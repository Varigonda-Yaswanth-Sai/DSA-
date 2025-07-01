"""
Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the answer fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.
Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.
Input: arr[] = [2, 3, 4] 
Output: 24 
Explanation: For an array with all positive elements, the result is product of all elements. 
Constraints:
1 ≤ arr.size() ≤ 106
-10  ≤  arr[i]  ≤  10


"""
import java.util.*;
class Solution {
    int maxProduct(int[] arr) {
        // code here
        int max=Integer.MIN_VALUE;
        int product=1;
        for(int i=0;i<arr.length;i++){
            product*=arr[i];
            max=Math.max(max,product);
            if(product==0){
                product=1;
            }
        }
        product=1;
        for(int i=arr.length-1;i>=0;i--){
            product*=arr[i];
            max=Math.max(max,product);
            if(product==0){
                product=1;
            }
        }
        return max;
    }
}
class Main {
    public static void main(String[] args){
        Solution mysol=new Solution();
        int arr[]={-1, -3, -10, 0, 6};
        System.out.println("Maximum product of the subarray is : "+ mysol.maxProduct(arr));
    }
}