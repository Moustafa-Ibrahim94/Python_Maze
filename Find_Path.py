import queue

def Maze():
    maze = []
    maze.append([False, False, False, False, False, "A", False, False, False])
    maze.append([False, True, True, True, True, True, True, True, False])
    maze.append([False, True, False, False, True, False, False, True, False])
    maze.append([False, True, False, True, True, True, False, True, False])
    maze.append([False, True, False, True, False, True, False, True, False])
    maze.append([False, True, False, True, False, True, False, True, False])
    maze.append([False, True, False, True, False, True, False, False, False])
    maze.append([False, True, True, True, True, True, True, True, False])
    maze.append([False, False, False, False, False, False, False, "B", False])

    return maze


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "A":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    path = []
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                path.append([j, i])
            else:
                pass
    return print(path)


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "A":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif maze[j][i] == False:
            return False
    return True


def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "A":
            start = x
    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1

    if maze[j][i] == "B":
        #print("Found: " + moves)
        printMaze(maze, moves)
        return True
    else:
        return False


# MAIN ALGORITHM



def main_function():
    nums = queue.Queue()
    nums.put("")
    add = ""
    maze = Maze()
    iter = 0
    while not findEnd(maze, add):
        add = nums.get()
        # print(add)
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(maze, put):
                nums.put(put)
        iter += 1
        if iter >= 80000:
            print("Not Found")
            break

main_function()