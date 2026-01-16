class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        MOD = 10**9 + 7
        
        # Add real boundaries
        h = [1] + hFences + [m]
        v = [1] + vFences + [n]
        
        h.sort()
        v.sort()
        
        # All possible horizontal gaps
        h_gaps = set()
        for i in range(len(h)):
            for j in range(i):
                h_gaps.add(h[i] - h[j])
        
        max_side = 0
        
        # Check vertical gaps
        for i in range(len(v)):
            for j in range(i):
                gap = v[i] - v[j]
                if gap in h_gaps:
                    max_side = max(max_side, gap)
        
        # Max usable side is limited by field size
        max_side = min(max_side, m - 1, n - 1)
        
        if max_side <= 0:
            return -1
        
        return (max_side * max_side) % MOD
