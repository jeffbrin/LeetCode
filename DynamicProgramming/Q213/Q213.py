class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        return max(
            nums[0] + self.rob_w_info(nums, 0, 2),
            nums[1] + self.rob_w_info(nums, 1, 3),
            self.rob_w_info(nums, 2, 2)
        )

    def rob_w_info(self, nums: List[int], picked: int, i: int = 0):
        """picked indicates which of the first two elements were picked."""

        try:
            return self.memo[(picked, i)]
        except KeyError:
            pass

        length = len(nums)

        if i >= length - 2:
            if i >= length:
                return 0
            elif i == length - 1:
                if picked > 0:
                    return nums[i]
                else:
                    return 0
            elif i == length - 2:
                if picked == 1:
                    return max(nums[i], nums[i+1])
                else:
                    return nums[i]

        res = max(
            nums[i] + self.rob_w_info(nums, picked, i+2),
            nums[i+1] + self.rob_w_info(nums, picked, i+3),
            nums[i] + self.rob_w_info(nums, picked, i+3)
        )
        self.memo[(picked, i)] = res
        return res
