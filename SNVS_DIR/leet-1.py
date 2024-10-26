class Solution(object):
    def countMaxOrSubsets(self, nums):
        # Calculate max OR value
        max_or = 0
        for n in nums:
            max_or |= n  # Corrected the syntax error here

        res = [0]  # Using a list to store the result, so it can be mutable

        # Define the dfs function
        def dfs(i, cur_or):
            if i == len(nums):  # Base case: if we've gone through all elements
                if cur_or == max_or:  # Check if the current OR equals max OR
                    res[0] += 1  # Modify the result using a mutable object
                return

            # Explore both possibilities: include or exclude the current number
            dfs(i + 1, cur_or)  # Exclude the current number
            dfs(i + 1, cur_or | nums[i])  # Include the current number

        # Start the dfs with index 0 and OR value 0
        dfs(0, 0)
        return res[0]  # Return the result stored in the list

