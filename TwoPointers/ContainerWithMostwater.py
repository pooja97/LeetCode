class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0 
        i = 0 
        j = len(height)-1 

        while(i<j):
            w = abs(j-i)
            h = min(height[i],height[j])
            maxWater = max(maxWater,(w*h))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1 
        return maxWater
    
''' using two pointer technique and moving the pointer with the smallest value after calculating the water level at the block. 
Run Time: O(n) since we are doing single pass 
Space Complexity: O(1)  no additional memory space is used '''