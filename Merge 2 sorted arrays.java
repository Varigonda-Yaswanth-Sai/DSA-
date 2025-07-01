/*Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.

Examples:

Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
Output:
2 2 3 4
7 10
Explanation: After merging the two non-decreasing arrays, we get, 2 2 3 4 7 10
Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
Output:
1 2 3 5 8 9
10 13 15 20
Explanation: After merging two sorted arrays we get 1 2 3 5 8 9 10 13 15 20.
Input: a[] = [0, 1], b[] = [2, 3]
Output:
0 1
2 3
Explanation: After merging two sorted arrays we get 0 1 2 3.
Constraints:
1 <= a.size(), b.size() <= 105
0 <= a[i], b[i] <= 107
*/

import java.util.*;
class Solution {
    // swap if arr1[i]>arr2[j]
    private void swapIfGreater(int arr1[],int arr2[],int i,int j){
        if(arr1[i]>arr2[j]){
            int temp=arr1[i];
            arr1[i]=arr2[j];
            arr2[j]=temp;
        }
    }
    public void mergeArrays(int arr1[],int arr2[]){
        int n=arr1.length;
        int m=arr2.length;
        int len=n+m;
        int gap=(len/2)+(len%2);
        // initial gap
        while(gap>0){
            int left=0;
            int right=left+gap;
            while(right<len){
                // arr1 and arr2
                if(left<n && right>=n){
                    swapIfGreater(arr1,arr2,left,right-n);
                }
                // both in arr2
                else if(left>=n && right<len){
                    swapIfGreater(arr2,arr2,left-n,right-n);
                }
                // both in arr1
                else{
                    swapIfGreater(arr1,arr1,left,right);
                }
                left++;right++;
            }
            // reduce gap for next iteration
            if(gap==1) break;
            gap=(gap/2)+(gap%2);
        }
    }
}
class Main {
    public static void main(String[] args){
        Solution mysol=new Solution();
        int arr1[]={2,4,7,10};
        int arr2[]={2,3};
        mysol.mergeArrays(arr1,arr2);
        System.out.println(Arrays.toString(arr1));
        System.out.println(Arrays.toString(arr2));
    }
}
