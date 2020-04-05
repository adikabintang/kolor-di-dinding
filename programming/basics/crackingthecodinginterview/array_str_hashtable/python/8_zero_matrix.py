def set_zero_matrix_v0(m: [[int]]):
    n_row = len(m)
    n_col = len(m[0])
    zero_points = []
    
    for r in range(n_row):
        for c in range(n_col):
            if m[r][c] == 0:
                zero_points.append((r, c))
    
    set_zero_points(m, zero_points)

def set_zero_points(m, zero_points):
    for point in zero_points:
        row = point[0]
        i = 0
        while i < len(m[row]):
            m[row][i] = 0
            i += 1
        
        col = point[1]
        i = 0
        while i < len(m):
            m[i][col] = 0
            i += 1

## more optimized

def set_all_row_0(m: [[int]], row: int):
    for c in range(len(m[row])):
        m[row][c] = 0

def set_all_column_0(m: [[int]], col: int):
    for r in range(len(m)):
        m[r][col] = 0

def set_zero_matrix_v1(m: [[int]]):
    row_has_0 = False
    col_has_0 = False
    n_row = len(m)
    n_col = len(m[0])

    for r in range(n_row):
        if m[r][0] == 0:
            col_has_0 = True
    
    for c in range(n_col):
        if m[0][c] == 0:
            row_has_0 = True
    
    for r in range(1, n_row):
        for c in range(1, n_col):
            if m[r][c] == 0:
                m[0][c] = 0
                m[r][0] = 0
    
    for r in range(n_row):
        if m[r][0] == 0:
            set_all_row_0(m, r)
    
    for c in range(n_col):
        if m[0][c] == 0:
            set_all_column_0(m, c)

    if row_has_0:
        set_all_row_0(m, 0)
    
    if col_has_0:
        set_all_column_0(m, 0)

## end of more optimized

matrix = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [19, 3, 67, 0]
]

set_zero_matrix_v0(matrix)
print(matrix)

matrix = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [19, 3, 67, 0]
]
set_zero_matrix_v1(matrix)
print(matrix)
