class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxi=max(candies)
        ans=[]
        for element in candies:
            if (maxi-element)<=extraCandies:
                ans.append(True)
            else:
                ans.append(False)
        return(ans)
        
