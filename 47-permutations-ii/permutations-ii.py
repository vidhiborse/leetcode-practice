class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        visited = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                result.append(list(path))
                return
            
            for i in range(len(nums)):
                # If already visited, skip
                if visited[i]:
                    continue
                
                # If this element is a duplicate of the previous one and the 
                # previous one hasn't been used in this branch, skip it to avoid duplicates.
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                
                # Choose
                visited[i] = True
                path.append(nums[i])
                
                # Explore
                backtrack(path)
                
                # Un-choose (Backtrack)
                path.pop()
                visited[i] = False
                
        backtrack([])
        return result