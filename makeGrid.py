def make_grid(width: int, height: int):
    i = 0
    ans = {j: set() for j in range(width * height)}
    for col in range(width):
        for row in range(height):
            lastCol = i % width >= width - 1
            lastRow = i // width >= height - 1
            # print(i, lastRow, lastCol)
            if lastRow and lastCol:
                # print("end")
                pass
            elif lastCol:
                ans[i].add(i + width)
                ans[i + width].add(i)
            elif lastRow:
                ans[i + 1].add(i)
                ans[i].add(i + 1)
            else:
                ans[i].add(i + 1)
                ans[i].add(i + width)
                ans[i + 1].add(i)
                ans[i + width].add(i)
            i += 1
    # This is much worse than the set implementation, and if you want to effectively test it you need to express the output as {int:set(int)}
    ansList = {key: [edge for edge in ans[key]] for key in ans}
    # To change to output to dict of sets, change output from ansList to ans
    return ansList


def test_make_grid_1():
    ans = make_grid(3, 2)
    correct = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}

    assert correct == ans


def test_make_grid_2():
    ans = make_grid(0, 0)
    correct = {}
    assert correct == ans


def test_make_grid_3():
    ans = make_grid(3, 3)
    correct = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [8, 2, 4],
        6: [3, 7],
        7: [8, 4, 6],
        8: [5, 7],
    }
    assert correct == ans
