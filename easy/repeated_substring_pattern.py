# Problem: 459. Repeated Substring Pattern
# Difficulty: Easy
#Time Complexity: O(n√n)

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s) 
        factors = set()
        #Get factors of n:
        for i in range(1,n//2 + 1):
            if n % i == 0:
                factors.add(i)
        
        for i in factors:
            #Only check for multiples of i len
            if s[0:i] * (int(n/i)) == s:
                return True
        return False