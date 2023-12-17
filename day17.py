from heapq import heappop, heappush
import fileinput

grid = [[int(c) for c in line.strip()] for line in fileinput.input()]
n = len(grid)
m = len(grid[0])

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve(mindist, maxdist):
	# cost, x, y, disallowedDirection
	q = [(0, 0, 0, -1)]
	seen = set()
	costs = {}
	
	while q:
		cost, y, x, old_dir = heappop(q)
		
		if x == m - 1 and y == n - 1:
			return cost
		
		if (y, x, old_dir) in seen:
			continue
		seen.add((y, x, old_dir))
		
		for dir in range(4):
			ncost = cost
			ny, nx = y, x
			
			if dir == old_dir or (dir + 2) % 4 == old_dir:
				continue
			direction = DIRS[dir]
            
			for distance in range(1, maxdist + 1):
				ny += direction[0]
				nx += direction[1]
				
				if 0 <= ny < n and 0 <= nx < m:
					ncost += grid[ny][nx]
					
					if distance < mindist or costs.get((ny, nx, dir), ncost+1) <= ncost:
						continue
					
					costs[(ny, nx, dir)] = ncost
					heappush(q, (ncost, ny, nx, dir))

print(solve(1, 3))
print(solve(4, 10))


				
                