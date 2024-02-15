class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dicp=[]
        dicn=[]
        ans=[]
        for i in nums:
            if i>0:
                dicp.append(i)
            else:
                dicn.append(i)
        for i in range(len(dicp)) :
            ans.append(dicp[i])
            ans.append(dicn[i])

        return(ans)
        
