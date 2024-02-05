class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        i=0
        ans = ''
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                ans = chr(int(s[i - 2:i]) + 96) + ans
                i = i - 3
            else:
                ans = chr(int(s[i]) + 96) + ans
                i = i - 1
        return ans      
