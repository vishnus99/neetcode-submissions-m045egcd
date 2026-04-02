class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        strs_sizes, result = [], ""
        for s in strs:
            strs_sizes.append(len(s))
        for size in strs_sizes:
            result += str(size)
            result += ','
        result += '#'
        for s in strs:
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for size in sizes:
            res.append(s[i:i + size])
            i += size
        return res
