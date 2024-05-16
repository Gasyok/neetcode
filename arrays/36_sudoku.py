from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                box = (i // 3) * 3 + j // 3
                if board[i][j] in hash:
                    for item in hash[board[i][j]]:
                        if item[0] == i or item[1] == j or item[2] == box:
                            return False
                    hash[board[i][j]].append((i, j, box))
                else:
                    hash[board[i][j]] = [(i, j, box)]
        return True
