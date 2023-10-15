class Solution(object):
    def canJump(self, nums):
        l=len(nums)
        max_reach=0
        for i in range(l):
            if i>max_reach:
                return False
            max_reach=max(max_reach,i+nums[i])
            if max_reach>=l-1:
                return True        