class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        for w in words:
            if all(w.count(c) <= chars.count(c) for c in w):
                result += len(w)
                

        return result
        