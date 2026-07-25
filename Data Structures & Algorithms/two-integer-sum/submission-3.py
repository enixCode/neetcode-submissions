class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, e in enumerate(nums):
                for i2, num in enumerate(nums):
                    if e + num == target and i != i2:
                        return [i, i2]
        return []