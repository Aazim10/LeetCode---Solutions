# I have two solutions for this.
# NO.1 has better Space Complexity
# NO.2 has better Time Complexity
# Solution 1
class Solution(object):
    def countNegatives(self,grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        neg_num = 0
        grid_rlen = len(grid)
        grid_clen = len(grid[0])
        for i in range(grid_rlen):
            lo = 0
            hi = len(grid[0])-1
            while lo<=hi:
                mid = (lo+hi)//2
                if grid[i][mid] < 0:
                    if (mid-1)>=0 and grid[i][mid-1]<0:
                        hi = mid - 1
                    else:
                        neg_num = neg_num + (grid_clen-mid)
                        lo = hi+1
                elif grid[i][mid] >= 0:
                    lo = mid + 1
        return neg_num

# Solution 2
class Solution(object):
    def countNegatives(self,grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        neg_num = 0
        grid_rlen = len(grid)
        grid_clen = len(grid[0])
        for i in range(grid_rlen):
            lo = 0
            hi = len(grid[0])-1
            while lo<=hi:
                mid = (lo+hi)//2
                mid_val =  grid[i][mid]
                if mid_val < 0:
                    if (mid-1)>=0 and grid[i][mid-1]<0:
                        hi = mid - 1
                    else:
                        neg_num = neg_num + (grid_clen-mid)
                        lo = hi+1
                elif mid_val >= 0:
                    lo = mid + 1
        return neg_num






        




        
