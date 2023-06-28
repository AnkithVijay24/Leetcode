class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            m = target-nums[i]
            if m in nums: 
                if nums.index(m) == i:
                    continue
                else:
                    if i in res:
                        continue
                        
                    else:
                        res.append(i)
                        res.append(nums.index(m))
        return res