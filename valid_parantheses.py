# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in hashMap:
                tp = stack.pop() if stack else '#'

                if hashMap[char] != tp:
                    return False
            else:
                stack.append(char)

        return not stack