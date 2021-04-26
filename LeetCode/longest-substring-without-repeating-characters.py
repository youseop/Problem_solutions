class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        hash = dict()
        max_len = 0
        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in hash and hash[char] >= left:
                left = hash[char]+1
            else:
                max_len = max(max_len,right-left+1)
            hash[char] = right
        return max_len