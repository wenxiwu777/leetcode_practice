class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 0
        l = len(nums)
        ret = []
        for i in range(0, l):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    ret.append(i)
                    ret.append(j)
                    break
        return ret