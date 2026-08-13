class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        stack = []

        for p in s:
            if p in pairs:
                if not stack or stack.pop() != pairs[p]:
                    return False
            else:
                stack.append(p)



        return not stack
        