
class Solution:
    def smallerNumbersThanCurrent(self, nums):

        # Step 1: Sort the array
        sorted_nums = sorted(nums)

        # Step 2: Store the first index of each number
        rank = {}

        for i, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = i

        # Step 3: Get answer according to original array
        result = []

        for num in nums:
            result.append(rank[num])

        return result