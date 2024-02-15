class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        #nums = [9,12,5,10,14,3,10]
        #pivot = 10
        ans=[]
        dic={"<pivot":[],
            "==pivot":[],
            ">pivot":[]  }

        #pivot=10
        for element in nums:
            if element<pivot:
                dic["<pivot"].append(element)
            elif element>pivot:
                dic[">pivot"].append(element)
            else:
                dic["==pivot"].append(element)

        combined_list = dic["<pivot"] + dic["==pivot"] + dic[">pivot"]
        return(combined_list)

        
