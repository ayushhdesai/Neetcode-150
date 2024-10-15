# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash, tHash = {}, {}

        if len(s) != len(t):
            return False
        else:
            for char in s:
                if char in sHash:
                    sHash[char] += 1
                else:
                    sHash[char] = 1

            for char in t:
                if char in tHash:
                    tHash[char] += 1
                else:
                    tHash[char] = 1

            if tHash == sHash:
                return True
            else:
                return False