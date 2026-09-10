# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def quickSortHelper(self, pairs: List[Pair], s: int, e:int) -> None:
        if e - s + 1 <= 1:
            return 
        
        pivot = pairs[e]
        start, left = s, s

        # Divide by pivot
        while s < e:
            if pairs[s].key < pivot.key:
                pairs[s], pairs[left] = pairs[left], pairs[s]
                left += 1
            s += 1
        if e != left:
            pairs[e], pairs[left] = pairs[left], pairs[e]

        self.quickSortHelper(pairs, start, left - 1)
        self.quickSortHelper(pairs, left + 1, e)

