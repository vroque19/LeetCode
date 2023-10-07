class Solution {
public:
    int climbStairs(int n) {
        std::vector<int> vec {1, 1};
        for(int i = 2; i <= n; i++) {
            vec.push_back(vec[i-2]+vec[i-1]);
        }
        int top = vec[n];
        vec.clear();
        return top;
    }
};