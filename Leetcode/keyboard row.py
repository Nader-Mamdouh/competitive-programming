class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        list1=["q","w","e","r","t","y","u","i","o","p"]
        list2=["a","s","d","f","g","h","j","k","l"]
        list3=["z","x","c","v","b","n","m"]
        #words = ["Hello","Alaska","Dad","Peace"]
        a=0
        b=0
        c=0
        ans=[]
        for word in words:
            for char in word:
                if char.lower() in list1:
                    a+=1
                elif char.lower() in list2:
                    b+=1
                else:
                    c+=1
            if len(word)==a or len(word)==b or len(word)==c:
                ans.append(word)
            a=0
            b=0
            c=0
        return(ans)
        
