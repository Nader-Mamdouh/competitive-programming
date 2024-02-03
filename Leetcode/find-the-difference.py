from collections import Counter

class Solution:
    def findTheDifference(self, s, t):
        count_s = Counter(s)
        count_t = Counter(t)

        for char, count in count_t.items():
            if count_s[char] != count:
                return char
