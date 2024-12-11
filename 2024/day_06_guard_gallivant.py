def parse_map(map_input):
    """Parse the input map into a 2D grid."""
    return [list(row) for row in map_input.strip().split('\n')]


def find_guard_start(grid):
    """Find the initial position and direction of the guard."""
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in directions:
                return x, y, cell, directions[cell]
    raise ValueError("No guard found in the map")


def turn_right(current_direction):
    """Determine the new direction after turning right."""
    turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    return turns[current_direction]


def is_valid_move(grid, x, y):
    """Check if the position is within the grid and not an obstacle."""
    return (0 <= y < len(grid) and
            0 <= x < len(grid[0]) and
            grid[y][x] != '#')


def simulate_guard_path(map_input):
    """Simulate the guard's patrol path."""
    # Parse the map
    grid = parse_map(map_input)

    # Find starting position and direction
    x, y, direction, (dx, dy) = find_guard_start(grid)

    # Track visited positions and original grid for marking
    visited = set([(x, y)])

    while True:
        # Check if there's an obstacle in the current direction
        next_x, next_y = x + dx, y + dy

        # If obstacle or out of bounds, turn right
        if not is_valid_move(grid, next_x, next_y):
            direction = turn_right(direction)
            # Update direction vector
            dx, dy = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}[direction]
            continue

        # Move forward
        x, y = next_x, next_y
        visited.add((x, y))

        # Check if guard is about to leave the mapped area
        if (x <= 0 or x >= len(grid[0]) - 1 or
                y <= 0 or y >= len(grid) - 1):
            break

    return len(visited)


# Read input from file
def solve_guard_patrol(filename):
    with open(filename, 'r') as file:
        map_input = file.read().strip()

    return simulate_guard_path(map_input)


if __name__ == "__main__":
    print(solve_guard_patrol('input/day_06.txt'))