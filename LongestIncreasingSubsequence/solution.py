#!/usr/bin/env python3

class Solution:
    def lengthOfLongestIncreasingSubsequence(self, nums: list[int]) -> int:
        lis = [1] * len(nums)

        for i in range(1, len(nums)):
            subs = [lis[j] for j in range(0, i) if nums[j] < nums[i]]
            lis[i] = 1 + max(subs, default=0)

        return max(lis, default=0)
