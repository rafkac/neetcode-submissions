from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = Counter(words[0])

        for w in words[1:]:
            counts &= Counter(w)
        
        return list(counts.elements())