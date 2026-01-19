class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])

        # prefix sum
        pre = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = (
                    mat[i - 1][j - 1]
                    + pre[i - 1][j]
                    + pre[i][j - 1]
                    - pre[i - 1][j - 1]
                )

        def possible(length):
            for i in range(length, m + 1):
                for j in range(length, n + 1):
                    total = (
                        pre[i][j]
                        - pre[i - length][j]
                        - pre[i][j - length]
                        + pre[i - length][j - length]
                    )
                    if total <= threshold:
                        return True
            return False

        left, right, ans = 0, min(m, n), 0

        while left <= right:
            mid = (left + right) // 2
            if possible(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
