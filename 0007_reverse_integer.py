class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negative_number = True
            x = abs(x)
        else:
            negative_number = False

        reversed_number = 0
        while x > 0:
            reversed_number = reversed_number * 10 + x % 10
            x = x // 10
        
        if negative_number:
            reversed_number = 0 - reversed_number
        if (0 - pow(2, 31)) <= reversed_number <= (pow(2, 31) - 1):
            return reversed_number
        else:
            return 0  
