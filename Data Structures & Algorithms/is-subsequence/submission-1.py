class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        target = t
        for char in s:
            if not char in target:
                return False
            else:
                target = target[target.find(char)+1:]
        return True


            

        