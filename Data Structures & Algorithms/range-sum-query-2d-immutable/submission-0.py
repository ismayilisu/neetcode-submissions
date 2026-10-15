class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m=len(matrix)
        self.n=len(matrix[0])
        self.pre=[[0 for _ in range(self.n+1)] for _ in range(self.m)]
        for i in range(self.m):
            temp=0
            for j in range(self.n):
                self.pre[i][j+1]=self.pre[i][j]+matrix[i][j]
        
                

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        sumi=0
        firstrowsumi=self.pre[row1][col1+1]-self.pre[row1][col2+1]
        lastrowsumi=self.pre[row2][col1+1]-self.pre[row2][col2+1]
        for j in range(row1,row2+1):
            sumi+=self.pre[j][col2+1]-self.pre[j][col1]
        return sumi
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)