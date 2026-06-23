class Solution:
    def search(self, nums: List[int], target: int) -> int:
        flag = False
        for i in nums:
            if i == target:
                flag = True
                return nums.index(i)
        if flag == False:
            return -1
    