# https://leetcode.com/problems/contains-duplicate/\

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) - len(set(nums)) != 0:
            return True
        else:
            return False        