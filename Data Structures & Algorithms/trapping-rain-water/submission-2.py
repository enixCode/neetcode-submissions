class Solution:
    def trap(self, height: List[int]) -> int:
        acc = 0
        max_level = max(height)
        for l in range(1, max_level+1):
            print(l)
            acc += self.gap(l, height)
        return acc

    def gap(self, level: int, heights: List[int]) -> int:
        acc = 0
        f_index = None
        for i, h in enumerate(heights):
            if f_index is None and len(heights)-i-1 == 0:
                    break
            if f_index is not None and h >= level:
                acc += i - f_index - 1
                print(f_index, i)
                f_index = None
            if f_index is None and h >= level and not len(heights)-i-1 == 0:
                if heights[i+1] < level:
                    f_index = i
                    print(f_index)
        return acc