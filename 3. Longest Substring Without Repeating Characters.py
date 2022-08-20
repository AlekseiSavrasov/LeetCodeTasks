# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_main = []
        max_sub_test = []

        for i in s:
            if i in max_sub_test:
                max_sub_test = max_sub_test[max_sub_test.index(i) + 1:]
                max_sub_test.append(i)
            else:
                max_sub_test.append(i)

            if len(max_sub_test) > len(max_sub_main):
                max_sub_main = max_sub_test
        return len(max_sub_main)
