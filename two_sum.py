class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}  # Hash table to store elements and their indices
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
            print(num_map)
        return []  # No solution found
# 2, 7, 11, 5
# 9
solution = Solution()
solution.twoSum([2, 7, 11, 5], 9)