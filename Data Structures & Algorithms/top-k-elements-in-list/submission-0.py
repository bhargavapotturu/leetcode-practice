class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newDict = {}

        for i in nums:
            if i in newDict:
                newDict[i]+=1
            else:
                newDict[i] = 0
        
        ans = []
        while len(ans) < k:
            largestKey = max(newDict, key=newDict.get)
            ans.append(largestKey)
            newDict.pop(largestKey)
    
        return ans
