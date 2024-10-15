# https://leetcode.com/problems/valid-palindrome/description/

import re

def cleanStr(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    s = s.lower()
    return s

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = cleanStr(s)
        l, r = 0, len(cs) - 1

        while l < r:
            if cs[l] != cs[r]:
                return False
            l += 1
            r -= 1
        
        return True