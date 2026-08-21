class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t = {}
        map_t_to_s = {}

        for s_char, t_char in zip(s, t):
            # If a mapping exists and it doesn't match the current character, it's invalid
            if (s_char in map_s_to_t and map_s_to_t[s_char] != t_char) or \
               (t_char in map_t_to_s and map_t_to_s[t_char] != s_char):
                return False
            
            # Create the mapping in both directions
            map_s_to_t[s_char] = t_char
            map_t_to_s[t_char] = s_char

        return True
        