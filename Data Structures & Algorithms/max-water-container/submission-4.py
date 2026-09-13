class Solution:
    def maxArea(self, heights: List[int]) -> int:
#       res = 0
#       for i in range(len(heights)):
#           for j in range(i+1,len(heights)):
#               smallest = min(heights[i], heights[j])
#               if res <  smallest*(j-i): 
#                   res = smallest*(j-i)
#       return res
        left = 0
        right = len(heights)-1
        res = 0
        while left < right:
            smallest = min(heights[left], heights[right])
            res = max(res, smallest*(right-left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res
                
            