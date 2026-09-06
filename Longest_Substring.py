'''Longest Substring Without Repeating Characters'''
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         last_seen = {}
#         l=0
#         max_length=0
#         for r in range(len(s)):
#             if s[r] in last_seen:
#                 l=max(last_seen[s[r]], l)
#             last_seen[s[r]]=r+1
#             max_length=max(max_length, r-l+1)
#         return max_length






'''Longest Substring Without Repeating Characters'''

s = "abcabzncbb"
max=""
for i in range(len(s)):
  c=""
  for j in range(i,len(s)):
    if s[j] not in c:
      c=c+s[j]
    else:
      break
  if len(max) < len(c):
    max=c
print(max)  