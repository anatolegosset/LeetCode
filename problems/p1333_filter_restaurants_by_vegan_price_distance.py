class Solution:
    def filterRestaurants(self, restaurants: list[list[int]], veganFriendly: int, maxPrice: int, maxDistance: int):
        return (r1[0] for r1 in sorted(filter(lambda r: (not veganFriendly or r[2]) and r[3] <= maxPrice and r[4] <= maxDistance, restaurants), key=lambda r: (r[1], r[0]), reverse=True))
