class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        elems = [1 for n in nums]
        for i, e in enumerate(nums):
            acc = 1
            for index, elem in enumerate(nums):
                if index != i:
                    elems[i] = elems[i] * elem
        return elems