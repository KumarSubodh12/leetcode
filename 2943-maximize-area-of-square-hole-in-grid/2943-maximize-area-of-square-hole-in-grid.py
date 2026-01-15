class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        def max_consecutive(bars):
            bars.sort()
            longest = cur = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    cur += 1
                else:
                    cur = 1
                longest = max(longest, cur)
            return longest + 1

        max_h = max_consecutive(hBars)
        max_v = max_consecutive(vBars)
        side = min(max_h, max_v)
        return side * side
