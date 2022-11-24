class Solution {
    fun reverse(x: Int): Int {
        var res = 0
        var n = x
        while (n != 0) {
            if (Math.abs(res) > Int.MAX_VALUE/10) return 0

            res = res*10 + n % 10
            n /= 10
        }
        return res
    }
}
