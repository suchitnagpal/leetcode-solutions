#Problem: 459. Repeated Substring Pattern
#Difficulty: Easy
#Time complexity: O(n√n)


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s) 
        factors = set()
        #Get factors of n:
        for i in range(1,n//2 + 1):
            if n % i == 0:
                factors.add(i)
        
        for i in factors:
            print(s[0:i] * (int(n/i)))
            if s[0:i] * (int(n/i)) == s:
                return True
        return False