class Solution(object):
    
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        modified_string = address.replace('.', '[.]')
        return(modified_string) 
   
