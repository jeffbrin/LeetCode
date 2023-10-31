class Solution:
    def climbStairs(self, n: int) -> int:
        j = 1
        k = 1
        sm = 1

        for x in range(1, n):
            sm = j + k
            j = k
            k = sm

        return sm
