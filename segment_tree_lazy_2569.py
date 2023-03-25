class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums1)
        st = [0]*(N*4+20)
        lazy = [1]*(N*4+20)

        def build(o: int, l: int, r: int):
            if l == r:
                st[o] = nums1[l-1]
            else:
                m = (l+r) >> 1
                build(o*2, l, m)
                build(o*2+1, m+1, r)
                st[o] = st[o*2+1]+st[o*2]

        def modify(o: int, l: int, r: int, L: int, R: int, k: int, lz: int):
            t = lazy[o]
            if l >= L and r <= R:
                if lz*k == -1:
                    st[o] = (r-l+1-st[o])
                    lazy[o] *= lz*k
            elif R < l or r < L:
                if lz == -1:
                    st[o] = (r-l+1-st[o])
                    lazy[o] *= lz
            else:
                m = (l+r)//2
                if L <= m:
                    modify(o*2, l, m, L, R, k, lz*lazy[o])
                else:
                    modify(o*2, l, m, L, R, 1, lz*lazy[o])
                if R >= m+1:
                    modify(o*2+1, m+1, r, L, R, k, lz*lazy[o])
                else:
                    modify(o*2+1, m+1, r, L, R, 1, lz*lazy[o])
                st[o] = st[o*2+1]+st[o*2]
                lazy[o] = 1

        build(1, 1, N)
        ans = []
        cursum = sum(nums2)
        for q in queries:
            if q[0] == 1:
                modify(1, 1, N, q[1]+1, q[2]+1, -1, 1)
            if q[0] == 2:
                cursum += q[1]*st[1]
            if q[0] == 3:
                ans.append(cursum)
        return ans
