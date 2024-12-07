class Solution {
    func isSquareRootInteger(_ num: Int) -> Bool {
        let sqrtVal = sqrt(Double(num))
        return sqrtVal.truncatingRemainder(dividingBy: 1) == 0
    }

    func judgeSquareSum(_ c: Int) -> Bool {
        var left = 0
        var right = Int(sqrt(Double(c)))

        while left <= right {
            let sum = left * left + right * right
            if sum == c {
                return true
            } else if sum < c {
                left += 1
            } else {
                right -= 1
            }
        }

        return false
    }
}
