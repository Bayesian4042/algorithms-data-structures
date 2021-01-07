class StockSpanner:

    def __init__(self):
        self.s = []
        self.indx = 0


    def next(self, price: int) -> int:
        
        weight = 1
        while(self.s and self.s[-1][0] <= price):
            weight += self.s.pop()[1]
        
        self.s.append((price, weight))
        return weight