class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct_s = []
        repeated = []
        for s in arr:
            if s not in distinct_s and s not in repeated:
                distinct_s.append(s)
            elif s in distinct_s:
                distinct_s.remove(s)
                repeated.append(s)
            
        if len(distinct_s) < k:
            return ""
        else:
            return distinct_s[k-1]

        