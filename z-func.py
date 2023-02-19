class Solution:
    def sumScores(self, s: str) -> int:
        n=len(s)
        z=[0]*n
        l,r=0,0
        for i in range(1,n):
            if i<=r and z[i-l]<r-i+1 :
                z[i]=z[i-l]
            else:
                z[i]=max(0,r-i+1)
                while i+z[i]<n and s[i+z[i]]==s[z[i]]:
                    z[i]+=1
                l,r=i,i+z[i]-1
        return sum(z)+n


#leetcode 2223