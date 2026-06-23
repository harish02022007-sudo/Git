class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            if i == 0:
                arr.append(nums[i])
            else:
                arr.append(sum(nums[0:i+1]))
        return arr