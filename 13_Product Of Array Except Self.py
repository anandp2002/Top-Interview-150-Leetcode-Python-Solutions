class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left_products = [1] * l
        right_products = [1] * l
        
        left_product = 1
        for i in range(l):
            left_products[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(l - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]
        
        answer = [left_products[i] * right_products[i] for i in range(l)]
        
        return answer