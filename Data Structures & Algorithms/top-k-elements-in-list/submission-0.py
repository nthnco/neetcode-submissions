class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sort = [[] for _ in range(len(nums) + 1)]
        answer = []
        map = {}
        count = k
        for val in nums:
            map[val] = map.get(val,0) + 1
        for key, val in map.items():
            sort[val].append(key)
        for i in range(len(sort) - 1, 0, -1):
            for j in sort[i]:
                if count > 0:
                    answer.append(j)
                    count -= 1
        return answer
