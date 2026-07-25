class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_numbers = len(numbers)
        for i, num in enumerate(numbers):
            for i2 in range(i+1, len_numbers):
                if num + numbers[i2] == target:
                    return [i+1, i2+1]