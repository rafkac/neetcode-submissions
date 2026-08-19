class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for w in words:
            for other_w in words:
                if w != other_w and w in other_w and w not in res:
                    res.append(w)
        return res
        