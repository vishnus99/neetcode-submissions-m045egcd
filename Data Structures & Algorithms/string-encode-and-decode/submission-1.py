class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        sizes, result = [], ""
        for s in strs:
            sizes.append(len(s))
        for size in sizes:
            result += str(size)
            result += ","
        result += "#"

        for s in strs:
            result += s
        
        return result
   
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        sizes, result, i = [], [], 0

        while s[i] != "#":
            curr = ""
            while s[i] != ",":
                curr += s[i]
                i += 1
            sizes.append(int(curr))
            i += 1
        i += 1

        for size in sizes:
            result.append(s[i:i + size])
            i += size
        return result