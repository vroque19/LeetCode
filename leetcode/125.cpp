#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        string sanitizedS = "";
        for(char c: s) {
            if (isalnum(c)) {
                char lower = tolower(c);
                sanitizedS += (tolower(c));
            }
            else {
                continue;
            }
        }
        
        for(int i = 0; i<sanitizedS.size(); i++) {
            int j = sanitizedS.size() - 1 - i;
            if(sanitizedS[i] != sanitizedS[j]) {
                return false;
            }
        }
        return true;
    }
};
