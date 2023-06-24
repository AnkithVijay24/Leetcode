class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        
        for i in range(len(candies)):
            sum = candies[i] + extraCandies
            print(sum)
            if sum >= max(candies):
                result.append(True)
                print(".")
            else:
                print(result)
                result.append(False)
                print(result)
                print(",")
        print(result)
        return result
