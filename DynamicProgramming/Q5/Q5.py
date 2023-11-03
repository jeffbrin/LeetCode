class Solution:
    
    def __init__(self) -> None:
        self.memo = {}

    def longestPalindrome(self, s: str) -> str:
        
        def expandAroundCenter(s: str, l: int, r: int) -> str:
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return s[l+1:r]

        max_pal = ""
        max_length = 0
        for i in range(len(s)):
            for offset in ((1, 1), (0, 1)):
                current = expandAroundCenter(s, i-offset[0], i+offset[1])
                current_length = len(current)
                if current_length > max_length:
                    max_pal = current
                    max_length = current_length
        
        return max_pal
