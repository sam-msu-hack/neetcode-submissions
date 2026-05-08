class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        new_list = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference not in sum_dict:
                sum_dict[difference] = i
        for i in range(len(nums)):
            if nums[i] in sum_dict and i != sum_dict[nums[i]]:
                new_list.append(min(i, sum_dict[nums[i]]))
                new_list.append(max(i, sum_dict[nums[i]]))
                return new_list