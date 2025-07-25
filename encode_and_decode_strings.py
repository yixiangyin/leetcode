# ------------------------------------------------------------
# Problem: 659 · Encode and Decode Strings
# URL: https://www.lintcode.com/problem/659/
# ------------------------------------------------------------
# Approach:
#   To encode: for each string, append "<len>#<str>"
#   To decode: scan through, read until '#', parse length, then recover substring
#
# Complexity:
#   Time:  O(m) for encode/decode
#   Space: O(m + n) for encode/decode
#   where m is the sum of length of all the strings and n is the number of strings
# ------------------------------------------------------------

class Solution:
    def encode(self, strs: list[str]) -> str:
        sol = ""
        for s in strs:
            sol = sol + str(len(s))+"#" + s
        return sol
    def decode(self, s: str) -> list[str]:
        sol = []
        while len(s) > 0:
            pos = s.find("#")
            count = int(s[:pos])
            sol.append(s[pos+1:pos+1+count])
            s = s[pos+1+count:]
        return sol

sol = Solution()
# input = ["lint","code","lo3#ve","you"]
input = ["a","b","a","c","d"]
print("input", input)
middle = sol.encode(input)
print("middle", middle)
output = sol.decode(middle)
print("output", output)
