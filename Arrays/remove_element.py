class Solution:
    def removeElement(self, nums, val) -> int:

        while val in nums:
            nums.remove(val)

        return len(nums)
