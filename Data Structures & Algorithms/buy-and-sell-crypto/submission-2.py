class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        lower = 101
        higher = None
        for i, n in enumerate(prices):
            if n < lower:
                if higher is not None:
                    profits.append(higher-lower)
                    print(profits)
                lower = n
                higher = n
                print('lower/reset', lower)
            if higher is not None and n > higher:
                higher = n
                print('high', n)
        profits.append(higher-lower)
        print(profits)
        return max(profits) if len(profits) > 0 else 0