class Solution:
    def check(self,lst: List[str])->bool:
        seen=set(lst)
        cnt=lst.count('.')
        if len(seen)==len(lst)-cnt+(1 if cnt>0 else 0) :
            return True
        return False
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            print(board[i])
            if self.check(board[i])==False:
                return False
        cols=list(zip(*board))
        for i in range(9):
            if self.check(cols[i])==False:
                return False
        for i in range(3):
            for j in range(3):
                rstart=3*i
                rend=3*(i+1)
                cstart=3*j
                cend=3*(j+1)
                subgrid=[row[cstart:cend] for row in board[rstart:rend]]
                lst=[]
                for r in subgrid:
                    lst.extend(r)
                if self.check(lst)==False:
                    return False
        return True
        