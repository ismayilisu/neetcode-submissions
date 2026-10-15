class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])
        dirc=[(-1,0),(1,0),(0,-1),(0,1)]
        #we got the destination 
        visited={}
        #startfrom the pacific waters
        q=deque([])
        for i in range(1,m):
            q.append((i,0))
            visited[(i,0)]=1
        for j in range(n):
            q.append((0,j))
            visited[(0,j)]=1
        #we got the startgin
        #just visiting is enoug
        while q:
            i,j=q.popleft()
            for dx,dy in dirc:
                nx,ny=i+dx,j+dy
                if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and heights[nx][ny]>=heights[i][j]:
                    q.append((nx,ny))
                    visited[(nx,ny)]=1
        q=deque([])
        ans=[]
        visited2={}
        for i in range(m):
            q.append((i,n-1))
            if (i,n-1) in visited:
                ans.append((i,n-1))
            visited2[(i,n-1)]=0
        for j in range(n-1):
            q.append((m-1,j))
            if (m-1,j) in visited:
                ans.append((m-1,j))
            visited2[(m-1,j)]=0
        while q:
            i,j=q.popleft()
            for dx,dy in dirc:
                nx,ny=i+dx,j+dy
                if 0<=nx<m and 0<=ny<n  and heights[nx][ny]>=heights[i][j] and (nx,ny) not in visited2:
                    if (nx,ny) in visited:
                        ans.append((nx,ny))
                    
                    q.append((nx,ny))
                    visited2[(nx,ny)]=1
        return ans
            

                    
            