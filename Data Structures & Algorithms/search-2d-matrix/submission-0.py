class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search middle row
        left = 0
        right = len(matrix) - 1
        print("left", left)
        print("right", right)


        while left <= right:
            mid_row = (left+right) // 2

            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                return self.search_row(matrix[mid_row], target)
            # if target is less than mid_row min, then search lower rows
            if matrix[mid_row][0] > target:
                right = mid_row - 1
            # if target is more than mid_row max, then search higher rows
            if matrix[mid_row][-1] < target:
                left = mid_row + 1

        return False

    # binary search through row
    def search_row(self, row: List[int], target) -> bool:
        left = 0
        right = len(row) - 1

        mid = len(row) // 2

        while left <= right:
            mid = (left+right) // 2
            if row[mid] == target:
                return True
            if row[mid] < target:
                left = mid+1
            if row[mid] > target:
                right = mid-1
        
        return False
                
