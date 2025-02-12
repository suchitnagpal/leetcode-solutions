# Problem: 875. Koko Eating Bananas
# Difficulty: Medium
#Time Complexity: O(nlogm)


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right: #O(log n)
            mid = (left + right) // 2
            summ = 0
            for i in piles: #O(m)
                summ += math.ceil(i/mid)
            if summ <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
