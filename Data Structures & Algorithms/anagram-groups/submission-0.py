class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newDict = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in newDict:
                newDict[key] = [word]
            else:
                newDict[key].append(word)
        
        finalList = []
        for key in newDict.keys():
            finalList.append(newDict[key])
        
        return finalList

