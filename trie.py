class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        trie=[{}]
        def get():
            trie.append({})
            return len(trie)-1
        for i in range(len(nums)):
            cnt,cur=0,0
            for j in range(i,len(nums)):
                if nums[j]%p==0:cnt+=1
                if cnt>k:break
                if nums[j] not in trie[cur]:
                    trie[cur][nums[j]]=get()
                cur=trie[cur][nums[j]]
        return len(trie)-1
#leetcode 2261