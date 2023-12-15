class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            current_height = min(height[l], height[r])
            max_area = max(max_area, current_height * (r-l))

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_area
