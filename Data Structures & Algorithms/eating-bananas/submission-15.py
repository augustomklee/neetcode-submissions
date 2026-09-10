class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (r + l) // 2
            if self.validEatingSpeed(piles, h, k):
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

    def validEatingSpeed(self, piles: List[int], h: int, k: int) -> bool:
        time = 0
        for p in piles:
            time += math.ceil(float(p) / k)
        return h  >= time
            
