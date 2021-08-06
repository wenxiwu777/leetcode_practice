class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret=''
        lcmp=list(strs[0])
        for i in range(0, len(lcmp)):
            eq=True
            for j in range(0, len(strs)):
                if len(strs[j]) == 0:
                    eq=False
                    break
                if i+1 > len(strs[j]):
                    eq=False
                    break
                if strs[j][i] != lcmp[i]:
                    eq=False
                    break
            if eq==True:
                ret+=lcmp[i]
            else:
                break
        return ret