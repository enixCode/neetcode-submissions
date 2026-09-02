class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, up = 0, len(nums)-1
        while low <= up:
            mid = low + (up-low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                up = mid -1
        return -1