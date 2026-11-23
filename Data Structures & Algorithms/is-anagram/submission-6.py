class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        char_dict = dict()

        for i in range(len(s)):
            if s[i] not in char_dict:
                char_dict[s[i]] = 1
            else:
                char_dict[s[i]] += 1

            if t[i] not in char_dict:
                char_dict[t[i]] = -1
            else:
                char_dict[t[i]] -= 1    
        
        for v in char_dict.values():
            if v != 0:
                return False
        return True
