class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        sumr = 0
        nu = str(n)
        for i in range(len(nu)):
            mul = mul * int(nu[i])
            sumr = sumr + int(nu[i])
        return mul - sumr
            
        