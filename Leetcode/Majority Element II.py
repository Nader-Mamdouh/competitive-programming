class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        dic={}
        ans=[]
        for element in nums:
            if element in dic:
                dic[element]+=1
            else:
                dic[element] =1
        for key,value in dic.items():
            if value>(n/3):
                ans.append(key)

        return(ans)
        
