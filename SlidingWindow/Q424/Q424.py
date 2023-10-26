class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        left = 0
        counts = {}
        max_len = 0
        max_chr = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1

            max_chr = max(max_chr, counts[s[right]])
            while right - left + 1 - max_chr > k:
                counts[s[left]] -= 1
                left += 1

            max_len = max(max_len, right-left+1)

        return max_len
