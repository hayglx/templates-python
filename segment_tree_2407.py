N=10**5
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        st=[0]*(N*4+20)
        def modify(o:int,l:int,r:int,Pos:int,Value:int):
            if l==r:
                st[o]=Value
            else:
                m=(l+r)//2
                if Pos<=m:
                    modify(o*2,l,m,Pos,Value)
                else:
                    modify(o*2+1,m+1,r,Pos,Value)
                st[o]=max(st[o*2+1],st[o*2])
            

        def query(o:int,l:int,r:int,L:int,R:int)->int:
            if l>=L and r<=R:
                return st[o]
            else:
                ans=0
                m=(l+r)//2
                if L<=m:
                    ans=max(ans,query(o*2,l,m,L,R))
                if R>m:
                    ans=max(ans,query(o*2+1,m+1,r,L,R))
                return ans

        for v in nums:
            L,R=max(1,v-k),v-1
            t=query(1,1,N,L,R) if L<=R else 0
            modify(1,1,N,v,t+1)
        return st[1]