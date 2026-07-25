class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tabl = {}
        for num in nums:
            if num not in tabl:
                tabl[num] = 0
            tabl[num] +=1
        tabl = sorted(list(tabl.items()), key=lambda n: n[1], reverse=True)
        tabl = tabl[:k]
        return [key for (key, val) in tabl]