class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        seen = set()
        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grid[(r // 3, c // 3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grid[(r // 3, c // 3)].add(board[r][c])
        
        return True
        

        