class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        l=list(s)
        l.reverse()
        restr=''.join(l)
        return (restr==s)