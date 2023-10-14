class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=dict(Counter(nums))
        for key in d:
            if d[key]>len(nums)/2:
                return key