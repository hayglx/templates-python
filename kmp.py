def strStr(self, haystack: str, needle: str) -> int:
    def getn(s:str)->List[int]:
        n=len(s)
        rt=[0]*n
        for i in range(1,n):
            j=rt[i-1]
            while s[i]!=s[j] and j!=0:
                j=rt[j-1]
            if s[i]==s[j]:
                j+=1
            rt[i]=j
        return rt
    n=getn(needle)
    i,j=0,0
    while i<len(haystack) and j<len(needle):
        if haystack[i]==needle[j]:
            i+=1
            j+=1
        elif j==0:
            i+=1
        else:
            j=n[j-1]
    return -1 if j!=len(needle) else i-j
                 