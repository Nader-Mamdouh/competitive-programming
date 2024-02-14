class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic1 = {}
        dic2 = {}

        for i in range(len(list1)):
            if list1[i] in list2:
                dic1[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in list1:
                dic2[list2[i]] = i

        for key, value in dic1.items():
            dic2[key] += value

        min_value = min(dic2.values())
        min_keys = [key for key, value in dic2.items() if value == min_value]

        return(min_keys)
        
