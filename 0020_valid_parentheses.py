class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "{": "}", "[": "]"}
        open_brackets = []
        for i in s:
            if i in bracket_map.keys():
                open_brackets.append(i)
            else:
                if len(open_brackets) == 0:
                    return False
                else:
                    if i != bracket_map[open_brackets[-1]]:
                        return False
                    else:
                        open_brackets = open_brackets[:-1]
        if len(open_brackets) != 0:
            return False
        return True
