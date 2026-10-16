class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        row=set()
        col=set()
        di1=set()
        di2=set()
        state= [[ '.' for _ in range(n)] for _ in range(n)]
        ans=[]
        def find(i,state):
            if i==n:
                ans.append([ ''.join(row) for row in state])
                return 
            
            for j in range(n):
                if  j not in col and i-j not in di1 and i+j not in di2:

                    col.add(j)
                    di1.add(i-j)
                    di2.add(i+j)
                    state[i][j]='Q'
                    find(i+1,state)
                    col.remove(j)
                    di1.remove(i-j)
                    di2.remove(i+j)
                    state[i][j]='.'
        find(0,state)
        return ans
            