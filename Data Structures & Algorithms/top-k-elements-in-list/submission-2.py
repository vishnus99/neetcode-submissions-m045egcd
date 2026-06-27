class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dict to count frequencies of each number
        count = {}
        #list where the index represents the frequency
        freq = [[] for i in range(len(nums) + 1)]

        #count numbers we have in the list
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        #iterate through our dictionary key, value pairs and add them to our frequency list
        for n, c in count.items():
            freq[c].append(n)
        
        #list to return final result
        final = []

        #go through our freq list backwards to grab the most frequent elements
        for i in range(len(freq) - 1, 0, -1):
            #go through each element in the sublist
            for num in freq[i]:
                final.append(num)
                #check if k elements have been grabbed
                if k == len(final):
                    return final
