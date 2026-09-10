class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       store = dict() 

       for i, n in enumerate(nums): 
            if n in store:
                return [store[n], i]
            store[target - n] = i 