class Solution:
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        print(counter)
        heap = []

        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))
        print(heap)
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
