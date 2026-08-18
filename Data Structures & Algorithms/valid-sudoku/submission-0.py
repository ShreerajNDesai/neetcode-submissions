class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            seen = set()
            for j in i:
                if j==".":
                    continue
                if j not in seen:
                    seen.add(j)
                else:
                    return False
        for i in range(9):
            seen = set()
            for j in board:
                if j[i]==".":
                    continue
                if j[i] not in seen:
                    seen.add(j[i])
                else:
                    return False
        for sqr in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (sqr//3) * 3 + i
                    col = (sqr % 3) * 3 + j
                    if board[row][col]==".":
                        continue
                    if board[row][col] not in seen:
                        seen.add(board[row][col])
                    else:
                        return False
        return True