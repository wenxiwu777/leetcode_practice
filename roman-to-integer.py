class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        l=len(s)
        sum=0
        while i<l:
            v,f=self.getValue(s,i)
            sum+=v
            if f==True:
                i+=1
            i+=1
        return sum

    def getValue(self, s, i):
        if s[i]=='I':
            if i+1<len(s):
                if s[i+1]=='V':
                    return [4,True]
                if s[i+1]=='X':
                    return [9,True]
            return [1,False]
        if s[i]=='V':
            return [5,False]
        if  s[i]=='X':
            if i+1<len(s):
                if s[i+1]=='L':
                    return [40,True]
                if s[i+1]=='C':
                    return [90,True]
            return [10,False]
        if s[i]=='L':
            return [50,False]
        if s[i]=='C':
            if i+1<len(s):
                if s[i+1]=='D':
                    return [400,True]
                if s[i+1]=='M':
                    return [900,True]
            return [100,False]
        if s[i]=='D':
            return [500,False]
        if s[i]=='M':
            return [1000,False]

if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt('IV'))



