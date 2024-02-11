class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        ans1=""
        ans2=""
        for item in word1:
            ans1+=item
        for item in word2:
            ans2+=item   
        if ans1==ans2:
            return True
        else:
            return False         
        
