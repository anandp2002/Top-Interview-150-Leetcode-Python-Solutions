class Solution(object):
    def removeElement(self, nums, val):
        l=len(nums)
        for i in range(l-1,-1,-1):
            if (nums[i]==val):
                nums.pop(i)
        return len(nums)