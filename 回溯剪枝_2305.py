class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        cs=[0]*k
        n=len(cookies)
        self.ans=inf
        def dfs(self,cur:int):
            if cur==n:
                self.ans=min(max(cs),self.ans)
            else:
                for i in range(min(cur+1,k)):
                    cs[i]+=cookies[cur]
                    dfs(self,cur+1)
                    cs[i]-=cookies[cur]
        dfs(self,0)
        return self.ans