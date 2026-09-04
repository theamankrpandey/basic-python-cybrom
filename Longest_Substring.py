'''Longest_Substring Without repeating character remove dublicate'''
a="helldfggohhhhdhdlijkmnb"


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count =0
        for i in range(0,len(s)-1):
            if s[i] == s[i+1]:
                count=count+1
            else:
                count=1
        print(count)
s=Solution()
s.lengthOfLongestSubstring("helldfggohhhhdhdlijkmnb")