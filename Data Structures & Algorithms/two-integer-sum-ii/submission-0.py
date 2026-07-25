class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            for i2 in range(i+1, len(numbers)):
                if num + numbers[i2] == target:
                    return [i+1, i2+1]