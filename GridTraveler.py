"""
Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to 
travel to the bottom-right corner. You only move down or right.

In how many ways can you travel to the goal on a gird with dimensions m * n?

Ex:

(2, 3)
 ______ ______ ________
| Start |      |       |
|______ |______|_______|
|       |      |   End |
|______ |______|_______|


"""



def grid_traveler(rows: int, columns: int)->int:
    if (rows == 1 and columns == 1):
        return 1
    if (rows == 0 or columns == 0):
        return 0
    
    return grid_traveler(rows-1, columns) + grid_traveler(rows, columns-1)


def enhanced_grid_traveler(rows: int, columns: int, memo: hash = {})->int:
    # Are the aguments in the memo
    key = str(rows) + ',' + str(columns)
    if(key in memo):
        return memo[key]
    
    if (rows == 1 and columns == 1):
        return 1
    if (rows == 0 or columns == 0):
        return 0
    
    memo[key] = enhanced_grid_traveler(rows-1, columns, memo) + enhanced_grid_traveler(rows, columns-1, memo)
    return memo[key]


# print(grid_traveler(1, 1))      # 1
# print(grid_traveler(2, 3))      # 3
# print(grid_traveler(3, 2))      # 3
# print(grid_traveler(3, 3))      # 6
# print(grid_traveler(18, 18))    # 2333606220


print(enhanced_grid_traveler(18, 18))    # 2333606220

print(enhanced_grid_traveler(25, 20))   