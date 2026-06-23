class Solution:
    def reverseWords(self, s: str) -> str:
        s =  s.split()
        # j = len(s)-1
        # arr = ""
        # for i in range(len(s)-1,-1,-1):
        #     arr += s[i] + " "
        # return arr.strip()

        return " ".join(s[::-1])