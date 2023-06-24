class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        i=0
        while i < len(candies):
            if candies[i] + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
            i+=1
        return result
