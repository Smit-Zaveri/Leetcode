class Solution:
    def isPalindrome(self, s: str) -> bool:
        pan = []
        for x in s:
            if x.isdigit() or x.isalpha():
                pan.append(x)
        strp  = "".join(pan)
        return strp.lower() == strp.lower()[::-1]