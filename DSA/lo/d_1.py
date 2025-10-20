from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for kom in operations:
            if kom == "X++" or kom == "++X":
                x += 1
            else:
                x -= 1
        return x

# ---- Input and Execution Part ----
# Example: Enter like this --> X++, ++X, X--, X++
ops = input("Enter operations separated by commas: ").split(",")
ops = [op.strip() for op in ops]  # remove extra spaces

sol = Solution()
result = sol.finalValueAfterOperations(ops)
print("Final value of X =", result)
