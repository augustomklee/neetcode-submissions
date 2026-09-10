class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute force: Count each char in strings. Ocurrences of chars should be equal.
        # Edge cases: 
        # both empty strings = true
        # casing doesn't matter
        # length != then return False
    
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else: count[c] = 1
    
        for c in t:
            if c in count:
                count[c] -= 1
            else: return False
        
        for c in count:
            if count[c] != 0:
                return False
        return True