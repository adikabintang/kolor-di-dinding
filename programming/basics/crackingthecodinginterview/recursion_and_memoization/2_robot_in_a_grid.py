# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

class Solution:
    def __init__(self):
        self.paths = []
        self.__forbidden_points = set([(1, 0)])

    def is_offlimit(self, row, column) -> bool:
        return (row, column) in self.__forbidden_points
    
    def find_path(self, start_row, start_column, end_row, end_column) -> ([(int, int)], bool):
        if start_row == end_row and start_column == end_column:
            return [(start_row, start_column)], True
        
        res = False
        path = []
        p = None
        if start_row + 1 <= end_row:
            if self.is_offlimit(start_row + 1, start_column) == False:
                p, res = self.find_path(start_row + 1, start_column, end_row, 
                    end_column)
        
        if res == False and (start_column + 1 <= end_column):
            if self.is_offlimit(start_row, start_column + 1) == False:
                p, res = self.find_path(start_row, start_column + 1, end_row, 
                    end_column)
        
        if res:
            path.append((start_row, start_column))
            path.extend(p)
        
        return path, res

s = Solution()
# print(s.find_path(0, 0, 2, 3))

# print(find_path(0, 0, 1, 1))
# print(find_path(0, 0, 1, 2))
print(s.find_path(0, 0, 100, 5))
