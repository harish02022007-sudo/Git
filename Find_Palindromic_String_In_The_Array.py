class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        flag = False
        for i in words:
            if i in words:
                temp = i
                s = i[::-1]

                if temp == s:
                    return temp

        if flag == False:
            return ""