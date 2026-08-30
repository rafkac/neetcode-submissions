class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        mapping = {}
        seen_words = set()

        for letter, w in zip(pattern, words):
            # if there is a mapping, check if it is not overwritng
            if letter in mapping:
                if mapping[letter] != w:
                    return False
            else:
                if w in seen_words:
                    return False

                mapping[letter] = w
                seen_words.add(w)


        return True