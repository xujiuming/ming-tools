from typing import List

'''
只有连续低收高买才是最高收益 
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            # 当前的大于前一天的 证明有盈利
            if prices[i - 1] < prices[i]:
                result += prices[i] - prices[i - 1]
        return result


if __name__ == '__main__':
    result = 0
    prices = [7, 6, 4, 3, 1]
    for i in range(1, len(prices)):
        # 当前的小于后一天的 证明有盈利
        if prices[i - 1] < prices[i]:
            result = result + (prices[i] - prices[i - 1])
    print(result)
