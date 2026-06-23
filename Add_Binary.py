class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        m = bin(a + b)
        return m[2:]