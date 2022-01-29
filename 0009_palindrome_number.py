class Solution:
    def isPalindrome(self, x: int) -> bool:
        # FLIP HALF NUMBER
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            reversed_number = 0
            while reversed_number < x:
                reversed_number = reversed_number * 10 + x % 10
                x = x // 10
            if reversed_number == x:
                return True
            else:
                if reversed_number // 10 == x:
                    return True
            return False
        
#         # FLIP FULL NUMBER
#         if x < 0 or (x % 10 == 0 and x != 0):
#             return False
#         else:
#             copy_x = x
#             temp_stack = []
#             while copy_x > 0:
#                 last_digit = copy_x % 10
#                 temp_stack.append(last_digit)
#                 copy_x = copy_x // 10

#             reversed_number = 0
#             ten_x = 0
#             while temp_stack:
#                 curr_digit = temp_stack.pop()
#                 reversed_number += curr_digit * (10 ** ten_x)
#                 ten_x += 1
#             if reversed_number == x:
#                 return True
#             else:
#                 return False
                
        
#         # STRING CONVERSION
#         if x < 0:
#             return False
#         else:
#             string_x = str(x)
#             left, right = 0, len(string_x) - 1
#             while right >= left:
#                 if string_x[left] == string_x[right]:
#                     left += 1
#                     right -= 1
#                 else:
#                     return False
#             return True
