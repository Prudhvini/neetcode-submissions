class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
         
        if image[sr][sc] == color:
            return image
        m = len(image)
        n = len(image[0])

        dirs = [(-1,0), (0,-1), (0,1), (1,0)]
        def dfs(r, c, orig):
            if not(0<=r<m) or not(0<=c<n) or image[r][c]!=orig:
                return
            image[r][c]=color
            for dr, dc in dirs:
                dfs(r+dr, c+dc, orig)
        dfs(sr,sc, image[sr][sc])
        return image

        
       