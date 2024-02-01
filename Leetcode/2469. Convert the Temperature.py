#https://leetcode.com/problems/convert-the-temperature/submissions/1163293449/
class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        list=[]
        list.append(kelvin)
        list.append(Fahrenheit)
        return list
