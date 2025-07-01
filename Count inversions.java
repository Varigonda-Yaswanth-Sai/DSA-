"""
Given an array of integers arr[]. Find the Inversion Count in the array.
Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.
Input: arr[] = [10, 10, 10]
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104

"""
import java.util.*;

class Solution {
    private static int merge(int arr[],int low,int mid,int high){
        ArrayList<Integer> temp=new ArrayList<> (); //temporary array
        int left=low; //starting idx left half of array
        int right=mid+1; //starting idx of right half of array
        int count=0; //count variable to count pairs
        while(left<=mid && right<=high){ //storing elements in temp array
            if(arr[left]<=arr[right]){
                temp.add(arr[left]);
                left++;
            }
            else{
                temp.add(arr[right]);
                count+=(mid-left+1);
                right++;
            }
        }
        // if elements on the left part is left
        while(left<=mid){
            temp.add(arr[left]);
            left++;
        }
        // if elements on right part is left
        while(right<=high){
            temp.add(arr[right]);
            right++;
        }
        // getting back all elements back to array from temp
        for(int i=low;i<=high;i++){
            arr[i]=temp.get(i-low);
        }
        return count;
    }
    public static int mergeSort(int arr[],int low,int high){
        int count=0;
        if (low>=high) return count;
        int mid=(low+high)/2;
        count+=mergeSort(arr,low,mid); //left half
        count+=mergeSort(arr,mid+1,high); //right half
        count+=merge(arr,low,mid,high); //merging sorted halves
        return count;
    }
    public static int countInversionPairs(int arr[]){
        int n=arr.length;
        // count number of pairs in an array
        return mergeSort(arr,0,n-1);
    }
}
public class Main {
    public static void main(String[] args){
        int arr[]={2,4,1,3,5};
        int count=Solution.countInversionPairs(arr);
        System.out.println("The Number of Inversion pairs are : "+count);

    }
}