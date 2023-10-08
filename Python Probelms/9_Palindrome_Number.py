class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        n = len(x) // 2
        palin = True
        r = -1
        for i in range(n):
            if x[i] != x[r]:
                return False
            else:
                r -= 1
        return palin
        
