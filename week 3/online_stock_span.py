# Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.
# The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.
# For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

# Note:

# Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
# There will be at most 10000 calls to StockSpanner.next per test case.
# There will be at most 150000 calls to StockSpanner.next across all test cases.

class StockSpanner:

    def __init__(self):
        self.l = []    

    def next(self, price: int) -> int:
        stockSpan = 1
        start = len(self.l) - 1
        if start == -1:
            self.l.append((price, 1))
            return 1
        while start >= 0 and self.l[start][0] <= price:
            stockSpan += self.l[start][1]
            self.l.pop()
            start -= 1

        self.l.append((price, stockSpan))
        return stockSpan