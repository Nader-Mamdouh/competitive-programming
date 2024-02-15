class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list=s.split()
        n=len(list)
        ans=""
        for i in range(n-1,-1,-1):
            if list[0] != " " or list[n-1] != " " :
                ans+=list[i]
            if i !=0:
                ans+=" "    
                
        return(ans)
