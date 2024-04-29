class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverse = 0
        while temp > 0:
            remainder = temp % 10
            reverse = (reverse * 10) + remainder
            temp = temp // 10
        return x == reverse