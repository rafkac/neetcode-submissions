class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        first_word = strs[0]
        max_length = len(first_word)

        prefix = ""
    
        for j in range(max_length):
            letter = first_word[j]
            # check if the letter repeats in every word
            if all(letter == s[j] for s in strs):
                prefix += letter
            else:
                break

        return prefix
            