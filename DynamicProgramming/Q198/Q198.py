class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def rob(self, nums: List[int], i: int = 0) -> int:
        
        length = len(nums)

        try:
            return self.memo[i]
        except KeyError:
            pass

        if i == length:
            return 0
        elif i == length - 1:
            return nums[i]
        elif i == length - 2:
            return max(nums[i], nums[i+1])
        elif i == length - 3:
            return max(nums[i] + nums[i+2], nums[i+1])
        
        result = max(
            nums[i] + self.rob(nums, i+2),
            nums[i+1] + self.rob(nums, i+3)
        )
        self.memo[i] = result
        return result
