class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        vector<int> ans(2);
        for(auto i = 0; i<nums.size(); i++) {
            int complement = target - nums[i];
            if(mp.find(complement)!= mp.end()) {
                ans[0] = mp[complement];
                ans[1] = i;
                return ans;
            }
            mp[nums[i]] = i;
        }
        return {};
    }
};
