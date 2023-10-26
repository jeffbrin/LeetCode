class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        # Get the total count of each character in s1
        counts = {}
        for c in s1:
            counts[c] = counts.get(c, 0) + 1

        l = 0
        for r in range(len(s2)):
            try:
                counts[s2[r]] -= 1

                # If this character is part of s1 but presents too many of a character
                while counts[s2[r]] < 0:
                    counts[s2[l]] += 1
                    l += 1
            except KeyError:
                # Char not part s1
                while l < r:
                    counts[s2[l]] += 1
                    l += 1
                l += 1

            if r - l + 1 == len(s1):
                return True

        return False
