# ------------------------------------------------------------
# Problem: 238. Product of Array Except Self
# URL: https://leetcode.com/problems/product-of-array-except-self/
# ------------------------------------------------------------
# Approach productExceptSelf:
#   breaks the problem into 2 sub problem, [...,A,...] => product of nums before A and after A.
#   compute them seperately and then combine the solution
#
# Complexity:
#   Time:  O(n)  
#   Space: O(n) 
#   where n is the length of the nums
# Approach productExceptSelfOpt:
#   use sol array to store the prefix and once we grab the postfix we multiply
#
# Complexity:
#   Time:  O(n)  
#   Space: O(1) sol array not counted
#   where n is the length of the nums
# ------------------------------------------------------------

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-1-1, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
        for i in range(0, len(nums)):
            sol[i] = prefix[i] * postfix[i]
        return sol
    def productExceptSelfOpt(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(0, len(nums)):
            sol[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            sol[i] *= postfix
            postfix *= nums[i]
        return sol
