#1
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pool={}
        for idx,item in enumerate(nums):
            residual = target - item
            if residual in pool:
                res_idx = pool[residual]
                return [idx,res_idx] 
            else:
                pool[item]=idx