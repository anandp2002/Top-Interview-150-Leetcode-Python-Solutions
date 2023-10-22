
class Solution:
    def trap(self, height: List[int]) -> int:        
        if not height:
            return 0        
        ans = 0                
        l=0
        r=len(height)-1
        lmax = height[0]
        rmax = height[-1]        
        while l <=r:   

            lmax=max(lmax,height[l])
            rmax=max(rmax,height[r])

            if lmax <= rmax:
                ans += lmax - height[l]
                l += 1
            else:
                ans += rmax - height[r]
                r -= 1
                
        return ans