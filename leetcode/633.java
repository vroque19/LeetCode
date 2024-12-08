class Solution {
    public boolean judgeSquareSum(int c) {
       for(int i = 0; i <= Math.sqrt(c)+1; i++) {
        int diff = c - (i * i);
        int sqrtdiff = (int) Math.sqrt(diff);
        if (sqrtdiff*sqrtdiff == diff) {
            return true;
        }
       } 
       return false;
    }
}
