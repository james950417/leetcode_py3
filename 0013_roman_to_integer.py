class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        i = 0
        # SOLUTION 1
        while i < len(s):
            if (i < len(s) - 1) and (symbol_value_map[s[i+1]] > symbol_value_map[s[i]]):
                sum += (symbol_value_map[s[i+1]] - symbol_value_map[s[i]])
                i += 2
            else:
                sum += symbol_value_map[s[i]]
                i += 1
        return sum
    
        # SOLUTION 2
        # while i < len(s):
        #     if s[i] in ("I", "X", "C"):
        #         if s[i] == "I":
        #             if (i < len(s) - 1) and (s[i+1] in ("V", "X")):
        #                 sum += (symbol_value_map[s[i+1]] - symbol_value_map[s[i]])
        #                 i += 2
        #             else:
        #                 sum += symbol_value_map[s[i]]
        #                 i += 1
        #         elif s[i] == "X":
        #             if (i < len(s) - 1) and (s[i+1] in ("L", "C")):
        #                 sum += (symbol_value_map[s[i+1]] - symbol_value_map[s[i]])
        #                 i += 2
        #             else:
        #                 sum += symbol_value_map[s[i]]
        #                 i += 1
        #         else:
        #             if (i < len(s) - 1) and (s[i+1] in ("D", "M")):
        #                 sum += (symbol_value_map[s[i+1]] - symbol_value_map[s[i]])
        #                 i += 2
        #             else:
        #                 sum += symbol_value_map[s[i]]
        #                 i += 1
        #     else:
        #         sum += symbol_value_map[s[i]]
        #         i += 1
        # return sum
