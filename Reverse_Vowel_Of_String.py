class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vow = "aeiouAEIOU"
        i = 0
        j = len(s)-1

        while i < j:
            if s[i] in vow and s[j] in vow:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] not in vow:
                i += 1
            else:
                j -= 1
        return "".join(s)