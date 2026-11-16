class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(path, visited):
            # If the path has all elements, we found a complete permutation
            if len(path) == len(nums):
                result.append(list(path))
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                # Choose
                visited[i] = True
                path.append(nums[i])
                
                # Explore
                backtrack(path, visited)
                
                # Un-choose (Backtrack)
                path.pop()
                visited[i] = False
                
        backtrack([], [False] * len(nums))
        return result