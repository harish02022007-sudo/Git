class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        su = 0
        for i in range(len(accounts)):
            if sum(accounts[i]) > su:
                su = sum(accounts[i])
        return su