class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_sorted = "".join(sorted(s)) # n log n + n
        t_sorted = "".join(sorted(t)) # n log n + n

        # n
        for i in range(len(s_sorted)):
            if s_sorted[i] != t_sorted[i]:
                return False
        # space: O(n), time: O(n)
        return True