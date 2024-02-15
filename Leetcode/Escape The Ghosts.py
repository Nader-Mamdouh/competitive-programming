class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        me=[0,0]
        f1=abs(target[0]-0)+abs(target[1]-0)

        f2=[]
        for element in ghosts:
            x=abs(target[0] - element[0]) + abs(target[1] - element[1])
            f2.append(x)

        #flag = True
        for element in f2:
            if f1 >= element:
                #flag = False
                return False

        return True
