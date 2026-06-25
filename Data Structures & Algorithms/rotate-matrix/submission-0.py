class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #take transpose and mirror image across columns
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        print(matrix)
        for j in range(n//2):
            for i in range(n):
                matrix[i][j],matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]