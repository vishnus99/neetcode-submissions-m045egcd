class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original_length = len(nums)
        set_length = len(set(nums))
        if original_length != set_length:
            return True
        else:
            return False
        