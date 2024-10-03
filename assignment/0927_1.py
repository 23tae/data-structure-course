def is_stack_full():
    if top == SIZE - 1:
        return True
    return False


def is_stack_empty():
    if top == -1:
        return True
    return False


def push_stack(element):
    global stack, top

    if is_stack_full() == True:
        print("스택에 공간이 없습니다.")
        return
    stack[top + 1] = element
    top += 1


def pop_stack():
    global stack, top

    if is_stack_empty():
        return None

    data = stack[top]
    stack[top] = None
    top -= 1
    return data


def find_start(maze, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'e':
                return (j, i)
    return None


def is_valid_move(maze, rows, cols, visited, new_coordinates: tuple):
    x, y = new_coordinates
    if 0 <= x < rows and 0 <= y < cols and not visited[y][x]:
        if maze[y][x] == '0' or maze[y][x] == 'x':  # 빈 공간 또는 출구로 이동 가능
            return True
    return False


def dfs(maze):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    start_coordinates = find_start(maze, rows, cols)
    if start_coordinates is None:
        return False  # 입구가 없음

    push_stack(start_coordinates)
    visited[start_coordinates[1]][start_coordinates[0]] = True

    while not is_stack_empty():
        current = pop_stack()
        x, y = current

        if maze[y][x] == 'x':  # 출구에 도착한 경우
            return True

        # 이동 가능한 8 방향 (상, 하, 좌, 우, 대각선)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(maze, rows, cols, visited, (new_x, new_y)):
                push_stack((new_x, new_y))
                visited[new_y][new_x] = True
                print(f"현재 위치:{(new_x, new_y)}\t현재 스택:{stack}")

    return False  # 출구를 찾을 수 없는 경우


maze = [
    ['1', '1', '1', '1', '1'],
    ['e', '0', '1', '0', '1'],
    ['1', '1', '0', '1', '1'],
    ['1', '0', '0', 'x', '1'],
    ['1', '1', '1', '1', '1']
]

SIZE = 10
stack = [None] * SIZE
top = -1

if dfs(maze) == True:
    print("성공!")
else:
    print("실패!")
