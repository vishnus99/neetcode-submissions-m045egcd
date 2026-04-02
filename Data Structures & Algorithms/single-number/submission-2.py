from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        sorted_counter = list(reversed(count.most_common()))
        return sorted_counter[0][0]
