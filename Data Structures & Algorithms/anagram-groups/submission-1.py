class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary to store k: [ana_1, ana_2, etc.]
        # loop through the array of strings
        # figure out if the current string is an anagram of whatever k

        # can we do this without sorting? sorting would create m * n * log(n) time
        # optimal time is m * n, so this should be accomplished without needing to sort

        # one way is to use tuples as keys of the dict, since they're hashable
        # instantiate a tuple of 26 and populate with counts of chars

        anagrams_dict = dict()

        for string in strs:
            char_count = [0] * 26 # O(1)
            for char in string:
                char_val = ord(char) - ord('a')
                char_count[char_val] += 1
            char_count = tuple(char_count)
            if char_count not in anagrams_dict:
                anagrams_dict[char_count] = [string]
            else:
                anagrams_dict[char_count] = [*anagrams_dict[char_count], string]
  
        return list(anagrams_dict.values())
