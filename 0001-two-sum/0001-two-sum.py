class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            m = target - nums[i]
            if m in res and res[m] != i:
                return [i, res[m]]
            res[nums[i]] = i
