class Solution:
    def isPalindrome(self, x):
        num_str = str(x)
        reversed_str = num_str[::-1]
        return num_str == reversed_str
