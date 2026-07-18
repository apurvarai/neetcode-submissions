class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def onedvalid(lst):
            freq=collections.Counter(lst)
            for i,j in freq.items():
                if i!='.' and j>1:
                    return False
            return True
        for i in range(9):
            if not onedvalid(board[i]):
                return False
        for i in range(9):
            col=[row[i] for row in board]
            if not onedvalid(col):
                return False
        res,res1,res2=[],[],[]
        for i in range(0,3):
            for j in range(0,3):
                res.append(board[i][j])
                if len(res)==9:
                    if not onedvalid(res):
                        return False
            for j in range(3,6):
                res2.append(board[i][j])
                if len(res2)==9:
                    if not onedvalid(res2):
                        return False
            for j in range(6,9):
                res1.append(board[i][j])
                if len(res1)==9:
                    if not onedvalid(res1):
                        return False
        res,res1,res2=[],[],[]
        for i in range(3,6):
            for j in range(0,3):
                res.append(board[i][j])
                if len(res)==9:
                    if not onedvalid(res):
                        return False
            for j in range(3,6):
                res2.append(board[i][j])
                if len(res2)==9:
                    if not onedvalid(res2):
                        return False
            for j in range(6,9):
                res1.append(board[i][j])
                if len(res1)==9:
                    if not onedvalid(res1):
                        return False
        res,res1,res2=[],[],[]
        for i in range(6,9):
            for j in range(0,3):
                res.append(board[i][j])
                if len(res)==9:
                    if not onedvalid(res):
                        return False
            for j in range(3,6):
                res2.append(board[i][j])
                if len(res2)==9:
                    if not onedvalid(res2):
                        return False
            for j in range(6,9):
                res1.append(board[i][j])
                if len(res1)==9:
                    if not onedvalid(res1):
                        return False

        return True
        # for i in range(0,9):
        #     if i==3 or i==6:
        #         res=[]
        #     for j in range(0,9):
        #         if j==3 or j==6:
        #             res=[]
        #         res.append(board[i][j])
        #         if len(res)==9:
        #             if not onedvalid(res):
        #                  return False
              
        return True