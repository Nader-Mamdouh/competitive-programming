class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x=0
        for item in operations:
            if item=="++X" or item == "X++":
                x+=1
            else:
                x-=1
        return(x)
        
