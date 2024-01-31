class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = ["" for _ in range(n + 1)]

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result[i] = "FizzBuzz"
            elif i % 3 == 0:
                result[i] = "Fizz"
            elif i % 5 == 0:
                result[i] = "Buzz"
            else:
                result[i] = str(i)

        return result[1:]
