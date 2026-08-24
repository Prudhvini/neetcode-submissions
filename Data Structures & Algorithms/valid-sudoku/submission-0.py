class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r,c = 9,9
        
        for i in range(r):
            row_set = set()
            col_set = set()
            block_set = set()

            for j in range(c):
                r_num = board[i][j]
                c_num = board[j][i]
                b_num = board[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3]
                if (r_num != '.' and r_num in row_set) or (c_num != '.' and c_num in col_set) or (b_num != '.' and b_num in block_set):
                    return False
                if r_num != '.': row_set.add(r_num)
                if c_num != '.': col_set.add(c_num)
                if b_num != '.': block_set.add(b_num)
        return True
