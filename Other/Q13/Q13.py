class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        out = 0
        lkp = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        length = len(s)
        for i, c in enumerate(s):
            
            if i != length - 1:
                if c == "I":
                    if s[i+1] in {"V", "X"}:
                        out -= 1
                        continue
                elif c == "X":
                    if s[i+1] in {"L", "C"}:
                        out -= 10
                        continue
                elif c == "C":
                    if s[i+1] in {"D", "M"}:
                        out -= 100
                        continue
                
            
            out += lkp[c]

        return out