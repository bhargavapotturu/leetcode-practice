class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapNums = {}
        for i in nums:
            if i in mapNums:
                return True
            else: 
                mapNums[i] = i
        return False