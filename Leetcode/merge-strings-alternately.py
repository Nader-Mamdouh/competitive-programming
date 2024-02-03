class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
             
        size1 = len(word1)
        size2 = len(word2)
        ans=""
        st=0
        if (size1<size2):
            for i in range(size1):
                ans+=word1[i]
                ans+=word2[i]
                st=i
            for i in range(st+1,size2):
                ans+=word2[i]
        elif size2<size1:
            for i in range(size2):
                ans+=word1[i]
                ans+=word2[i]
                st=i
            for i in range(st+1,size1):
                ans+=word1[i]
        else:
            for i in range(size1):
                ans+=word1[i]
                ans += word2[i]

        return(ans)
