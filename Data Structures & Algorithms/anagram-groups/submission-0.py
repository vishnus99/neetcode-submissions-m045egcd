class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            hash[key].append(word)
        return list(hash.values())
                

            
        