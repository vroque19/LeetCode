#include <bits/stdc++.h>

class Solution {
public:
    vector<int>merge(vector<int>&left, vector<int>&right) {
        vector<int>new_arr;
        std::size_t i = 0;
        std::size_t j = 0;

        while( i < left.size() && j < right.size() ) {
            if( left[i] <= right[j] ) {
                new_arr.push_back(left[i]);
                i++;
            }
            else {
                new_arr.push_back(right[j]);
                j++;
            }
        }

        while( i < left.size() ) {
            new_arr.push_back(left[i]);
            i++;
        }
        while( j < right.size() ) {
            new_arr.push_back(right[j]);
            j++;
        }

        return new_arr;
    }
    
    vector<int> mergeSort(vector<int>&arr) {
        std::size_t length = arr.size();
        if(length <= 1) {
            return arr;
        }
        vector<int> left_half;
        vector<int> right_half;
        for( int i = 0; i < floor(length/2); i++) {
            left_half.push_back(arr[i]);
        }
        for( int i = floor(length/2); i < length; i++) {
            right_half.push_back(arr[i]);
        }

        left_half = mergeSort(left_half);
        right_half = mergeSort(right_half);

        return merge(left_half, right_half);
        }
    bool containsDuplicate(vector<int>& nums) {
        nums = mergeSort(nums);
        for( int i = 0; i < nums.size()-1; i++ ) {
            if( nums[i] == nums[i+1] ) {
                    return true;
                }
        }
        return false;
    }
};