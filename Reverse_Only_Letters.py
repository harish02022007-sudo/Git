class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s)-1
        while i < j:
            if ((chr(65) <= s[i] <= chr(90)) or (chr(97) <= s[i] <= chr(122))) and \
                ((chr(65) <= s[j] <= chr(90)) or (chr(97) <= s[j] <= chr(122))):
                s[i], s[j] = s[j], s[i]
                j -= 1
                i += 1
            elif chr(65) <= s[i] <= chr(90) or chr(97) <= s[i] <= chr(122):
                j -= 1
            elif chr(65) <= s[j] <= chr(90) or chr(97) <= s[j] <= chr(122):
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(s)