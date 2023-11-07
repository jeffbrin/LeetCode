# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """

#         if n < 5:
#             return self.climb_stairs(n)
#         else:
#             j = self.climb_stairs(4)
#             k = self.climb_stairs(5)
#             nxt = j + k

#             i = 0
#             while n - 5 >= i:
#                 nxt = j + k
#                 k = j
#                 j = nxt
#                 i += 1
#             return nxt

#     def climb_stairs(self, n, step=0) -> int:
#         """
#         Returns the total number of ways that the remaining steps can be climbed.
#         """

#         if step == n:
#             return 0
#         elif step == n-1:
#             return 0
#         else:
#             return self.climb_stairs(n, step+1) + self.climb_stairs(n, step+2) + 1


# s = Solution()
# print(s.climbStairs(2))
# print(s.climbStairs(3))
# print(s.climbStairs())

from typing import Optional
def value_to_subtract(c: str, s:str, i) -> Optional[int]:
    """ None means don't subtract """
    lkp = {
        "I": lambda: 1 if s[i+1] in {"V", "X"} else None
    }

    return lkp[c]()

print(value_to_subtract("I", "II", 0))
print(value_to_subtract("I", "IV", 0))
