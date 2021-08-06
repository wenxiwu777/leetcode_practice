class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True

        stack=[]
        l=list(s)
        ret=True
        while len(l)>0:
            c=l.pop()
            # ( { [ ] } )
            if (c==')') or (c=='}') or (c==']'):
                stack.append(c)
            elif (c=='(') or (c=='{') or (c=='['):
                if len(stack)==0:
                    ret=False
                    break
                s=stack.pop()
                if c=='(' and s!=')':
                    ret=False
                    break
                elif c=='{' and s!='}':
                    ret=False
                    break
                elif c=='[' and s!=']':
                    ret=False
                    break

        if ret==True:
            ret=((len(l)==0) and (len(stack)==0))

        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid('(()[]({}))'))
    