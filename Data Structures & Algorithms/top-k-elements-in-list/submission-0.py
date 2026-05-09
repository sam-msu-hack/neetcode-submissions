class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_list = []
        count_dict = {}
        for item in nums:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1
        sorted_count = sorted(count_dict.items(), key=lambda item: item[1], reverse= True)
        for i in range(k):
            new_list.append(sorted_count[i][0])
        return new_list