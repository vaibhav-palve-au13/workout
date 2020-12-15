def matrix_spiral_print(matrix):
  # Fill this in.
    if not matrix:
	    print("")

    R, C = len(matrix), len(matrix[0])
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    result = []
    seen = [[False]*C for _ in range(R)]
    row = 0
    col = 0
    di = 0
    for _ in range(R*C):
        result.append(matrix[row][col])
        seen[row][col] = True
        rr, cc = row + dr[di], col + dc[di]
        if 0 <= rr < R and 0 <= cc < C and not seen[rr][cc]:
            row, col = rr, cc
        else:
            di = (di+1)%4
            row, col = row + dr[di], col + dc[di]

    print(result)
    return 

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12