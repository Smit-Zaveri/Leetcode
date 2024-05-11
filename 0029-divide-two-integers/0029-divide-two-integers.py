class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = dividend/divisor
        a = str(floor(ans) if ans >= 0 else ceil(ans))
        if float(a) >= 2147483648:
            return int(a.split(".")[0])-1
        else:
            return int(a.split(".")[0])
        