class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = []
        new_nums = []
        for i in nums:
            if i == 0:
                zeros.append(i)
            else:
                new_nums.append(i)

        new_nums.extend(zeros)
        nums[:] = new_nums