class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # ok check rows maybe 2 loops one to stay on row
        # other to do the binary search
        
        for i in range(len(matrix)):
            l,r=0,len(matrix[0]) - 1 
            row = matrix[i]
            # ok when it is not found int that row can we move
            # to the next row like how?
            while l <= r:
                mid = (l+r)//2 
                if matrix[i][mid] > target:
                    r = mid - 1
                elif matrix[i][mid] < target:
                    l = mid + 1
                else:
                    return True
        return False