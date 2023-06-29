class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            sorted_strs = ''.join(sorted(s))

            if sorted_strs not in res:
                res[sorted_strs] = []

            res[sorted_strs].append(s)

        return list(res.values())