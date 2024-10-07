def valid(nx, ny, r, c):
    return 0 <= nx < r and 0 <= ny < c

def traverse_forest(r, c, N, forest, movements):
    x, y = 0, 0
    
    total_gems = forest[x][y]
    forest[x][y] = 0  # Emas di posisi awal diambil dan diset menjadi 0
    
    move_dict = {
        'L': (0, -1),
        'R': (0, 1),
        'D': (1, 0),
        'U': (-1, 0)
    }
    
    for move in movements:
        dx, dy = move_dict[move]
        nx, ny = x + dx, y + dy
        
        if not valid(nx, ny, r, c):
            return total_gems, "gerakanmu salah bung!"
        
        x, y = nx, ny
        
        if move in ['L', 'D']:
            total_gems -= 2 
        elif move in ['R', 'U']:
            total_gems += 3
        
        total_gems += forest[x][y]
        forest[x][y] = 0  # Emas di posisi saat ini diambil dan diset menjadi 0
    
    return total_gems, None

r, c, N = map(int, input().split())
forest = [list(map(int, input().split())) for _ in range(r)]
movements = input().strip()

result, error = traverse_forest(r, c, N, forest, movements)

if error:
    print(result)
    print(error)
else:
    print(result)