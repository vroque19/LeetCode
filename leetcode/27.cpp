#include<bits/stdc++.h>
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        nums.erase(std::remove(nums.begin(), nums.end(), val), nums.end());

        return std::size(nums);
    }
};