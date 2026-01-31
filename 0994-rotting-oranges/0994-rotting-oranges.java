class Pair {
    int row;
    int col;

    Pair(int _row, int _col) {
        this.row = _row;
        this.col = _col;
    }
}

class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] vis = new int[m][n];
        Queue<Pair> queue = new LinkedList<>();
        int fresh = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new Pair(i, j));
                    vis[i][j] = 1;
                }
                if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }

        int[] directionRow = {-1, 0, 1, 0};
        int[] directionCol = {0, 1, 0, -1};

        int ans = 0;

        while (queue.size() > 0) {
            int size = queue.size();
            boolean rotted = false;

            for (int it = 0; it < size; it++) {
                int row = queue.peek().row;
                int col = queue.peek().col;
                queue.poll();

                for (int i = 0; i < 4; i++) {
                    int newRow = row + directionRow[i];
                    int newCol = col + directionCol[i];

                    if (newRow >= 0 && newRow < m &&
                        newCol >= 0 && newCol < n &&
                        vis[newRow][newCol] == 0 &&
                        grid[newRow][newCol] == 1) {

                        queue.offer(new Pair(newRow, newCol));
                        vis[newRow][newCol] = 1;
                        rotted = true;
                        fresh--;
                    }
                }
            }
            if (rotted) ans++;
        }
        return fresh == 0 ? ans : -1;
    }
}