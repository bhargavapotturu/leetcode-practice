class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listAns = []
        dictNums = {}
        j = 0
        for i in nums:
            if target-i in dictNums:
                listAns.append(dictNums[target-i])
                listAns.append(j)
                return listAns
            dictNums[i] = j
            j+=1    

     
