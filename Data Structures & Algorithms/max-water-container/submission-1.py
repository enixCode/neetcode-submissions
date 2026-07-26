class Solution:
    def maxArea(self, heights: List[int]) -> int:
        index_f, index_l = None, None
        max_water = 0
        for i in range(len(heights)):
            for i2 in range(len(heights)-1, -1, -1):
                if i < i2 and i != i2:
                    w = self.water(heights[i], heights[i2], i2-i)
                    if w > max_water:
                        max_water = w
                        index_f, index_l = i, i2
        return max_water

    def water(self, first: int, last: int, x_len: int):
        h = first if first < last else last
        return x_len * h