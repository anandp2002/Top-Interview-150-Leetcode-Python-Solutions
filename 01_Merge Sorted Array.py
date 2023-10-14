class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l=m+n
        nums=nums1
        for i in range(l-1,m-1,-1):            
            nums1.pop(i)
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()