class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charDict = {}
        for i in s:
            charDict[i] = charDict.get(i, 0) + 1
        for i in t:
            if i not in charDict:
                return False
            charDict[i] -=1
            if charDict[i] == 0:
                del charDict[i]

        return len(charDict) == 0
