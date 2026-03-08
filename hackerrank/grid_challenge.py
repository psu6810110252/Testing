def gridChallenge(grid):
    # เรียงแต่ละแถวตามตัวอักษร
    sorted_grid = ["".join(sorted(row)) for row in grid]
    cols = len(sorted_grid[0])
    rows = len(sorted_grid)
    
    # เช็คแนวตั้ง
    for col in range(cols):
        for row in range(1, rows):
            if sorted_grid[row][col] < sorted_grid[row-1][col]:
                return "NO"
    return "YES"
