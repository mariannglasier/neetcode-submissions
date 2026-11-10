class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        doop_set = set()
        for num in nums:
            if num not in doop_set:
                doop_set.add(num)
            elif num in doop_set:
                return True
        return False