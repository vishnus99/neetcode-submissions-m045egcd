class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_square_digits(x: int) -> int:
            total = 0
            while x > 0:
                d = x % 10
                total += d * d
                x //=10 
            return total
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum_square_digits(n)
        return True
                
        

            
        
        