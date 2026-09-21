class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = 0
        map = {}
        answer = []
        for idx, val in enumerate(strs):
            sorted_list = sorted(val)
            sorted_word = ''.join(sorted_list)
            if sorted_word in map:
                answer[map[sorted_word]].append(val)
            else:
                answer.append([val])
                map[sorted_word] = count 
                count += 1
            
        return answer


