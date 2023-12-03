class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        if num:
            self.prefix_products.append(self.prefix_products[-1] * num)
        else:
            self.prefix_products = [1]

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_products):
            return 0
        else:
            return self.prefix_products[-1] // self.prefix_products[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)