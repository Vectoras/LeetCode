# Python - 412. Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results = []
        for x in range(1, n+1):
            if x % 3 == 0 and x % 5 == 0:
                results.append("FizzBuzz")
            elif x % 3 == 0:
                results.append("Fizz")
            elif x % 5 == 0:
                results.append("Buzz")
            else:
                results.append(str(x))
                
        return results