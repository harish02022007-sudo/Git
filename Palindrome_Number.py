# 9
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        temp = str(temp)
        a = temp[::-1]
        if temp == a:
            return True
        else:
            return False