class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in res:
                length = 0
                while n+length in res:
                    length+=1
                longest = max(longest, length)
        return longest