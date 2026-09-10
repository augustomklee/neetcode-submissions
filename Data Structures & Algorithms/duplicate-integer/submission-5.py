class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Empty or single item array: return true
        # Else check for duplicate
        # O(n) time and space

        count = set()
        for n in nums:
            if n in count:
                return True
            count.add(n)
        return False