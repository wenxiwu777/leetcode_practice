class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=str(x)
        is_neg=(s[0]=='-')        
        if is_neg==True:
            s2=s[1:]
            ls2=list(s2)
            ls2.reverse()
            rs=''.join(ls2)
            n=-int(rs)
            if n<-2**31:
                return 0
            return n
        else:
            ls=list(s)
            ls.reverse()
            rs=''.join(ls)
            n=int(rs)
            if n>2**31:
                return 0
            return n

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-426))