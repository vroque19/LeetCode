class Solution {
public:
    bool isUgly(int n) {
        // if the number has any factors that are prime other than 2, 3, 5 return false
        // if the number only has prime factors that are 2, 3, 5 or is prime, return true
        
        if(n <= 0) {
            return false;
        }
        if(n==1) {
            return true;
        }

        for(int i = 2; i <=5; i++) {
            // while we have a factor
            while(n%i == 0) {
                n/=i; // divide n by our divisor
            }
        }
        return n == 1;

      
    }
};
