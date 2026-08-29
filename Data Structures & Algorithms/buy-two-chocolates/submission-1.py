class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        i = 0
        og_money = money

        prices.sort()

        max_buy = 2
        while i < len(prices):
            if not max_buy <= 0 and money >= prices[i]:
                max_buy -= 1
                money -= prices[i]
            i += 1

        return og_money if max_buy > 0 else money
