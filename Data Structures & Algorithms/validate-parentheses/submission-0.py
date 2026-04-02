class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")": "(", "]": "[", "}": "{"}
        stack =[]
        
        for char in s:
            if char in pair.values():
                stack.append(char)
            elif char in pair.keys():
                if len(stack) == 0 or stack[-1] != pair[char]:
                    return False
                stack.pop()
            else:
                return False
        
        return len(stack) == 0 
        
            
        