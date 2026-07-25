class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print(nums)
        nums = sorted(nums)
        print(nums)
        
        nums = set(nums)
        print(nums)
        
        nums = list(nums)
        print(nums)

        nums = sorted(nums)
        print(nums)
        
        if len(nums) == 0:
            return 0
        acc = 0
        best = 0
        for i, num in enumerate(nums):
            if i > 0:
                if nums[i-1]+1 == nums[i] or nums[i-1]-1 == nums[i]:
                    print("nums", nums[i-1], nums[i])
                    acc += 1
                else:
                    best = acc if acc > best else best
                    print("best", best)
                    acc = 0
        best = acc if acc > best else best
        return best+1