import json


grid = json.loads(open('grid.json').read())



def print_grid():
    for line in grid:
        cc = ""
        for cell in line:
            cc += " {:1} ".format(cell)
        print(cc)


print_grid()
