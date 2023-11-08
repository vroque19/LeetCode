class Solution {
public:
    int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
        int total = 0;
        for (auto i: hours) {
            if (i < target) {
                continue;
            }
            else {
                total ++;
            }
        }
        return total;
    }
};