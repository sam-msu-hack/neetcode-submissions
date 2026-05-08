class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set()
        for item in nums:
            if item not in new:
                new.add(item)
            else:
                return True
        return False