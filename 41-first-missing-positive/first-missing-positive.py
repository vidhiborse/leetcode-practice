class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Place each number in its correct position if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]  # Swap
                
        # Step 2: Find the first index where the number doesn't match the index + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # Step 3: If 1 to n are all present, the answer is n + 1
        return n + 1