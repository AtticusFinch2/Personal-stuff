def make_grid(width:int, height:int):
    i=0
    ans = {j:[] for j in range(width*height)}
    for row in range(height):
        for col in range(width):
            print(row, col, i)
            if col == width-1 and row == height-1:
                pass
            elif row == height - 1:
                ans[i] = [i + 1]
                ans[i + 1].append(i)
            elif col == width - 1:
                ans[i] = [i + width]
                ans[i + width].append(i)
            else:
                ans[i] = [i+1, i+width]
                ans[i+1].append(i)
                ans[i+width].append(i)
            i+=1

    return ans
print(make_grid(3,2))