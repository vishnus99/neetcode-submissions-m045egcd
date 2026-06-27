class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[tuple[int, ...], list[str]] = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())
        
        


            