# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeRecursion(pairs, 0, len(pairs) - 1)


    def mergeRecursion(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1: # length one division
            return pairs

        m = (s + e) // 2
        # Sort left half
        self.mergeRecursion(pairs, s, m)

        # Sort right half
        self.mergeRecursion(pairs, m + 1, e)

        # Merge sorted halfs
        self.merge(pairs, s, m, e)

        return pairs

        # Merge in-place
    def merge(self, arr: List[Pair], s: int, m: int, e: int) -> None:
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]
        i = 0 # index for L
        j = 0 # index for R
        k = s # index for arr

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # If either L or R finish
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while i < len(L):
            arr[k] = R[j]
            j += 1
            k += 1











