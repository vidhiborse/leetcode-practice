class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We don't need to jump from the last index
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            # If we have reached the end of the current jump's range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Early exit if we can already reach or exceed the last index
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps