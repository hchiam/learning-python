def rot90(img):
    """assumes 2D array of NxN"""
    # for i in range(len(img))
    width = len(img)
    # shifting layers (changing column/row sizes)
    for j in range(width//2):
        # going across single layer (based on changing layer sizes from outer loop)
        for i in range(j, width-1-j):
            temp = img[j][i]
            img[j][i] = img[width-1-i][j]
            img[width-1-i][j] = img[width-1-j][width-1-i]
            img[width-1-j][width-1-i] = img[0+i][width-1-j]
            img[0+i][width-1-j] = temp
    return img


print('2x2 works: ',
    rot90(
    [
        [1,2],
        [3,4]
    ])
      
      ==
      
    [
        [3,1],
        [4,2]
    ]
)

print('3x3 works: ',
    rot90(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
      
      ==
      
    [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]
)

print('4x4 works: ',
    rot90(
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,0,1,2],
        [3,4,5,6]
    ])
      
      ==
      
    [
        [3,9,5,1],
        [4,0,6,2],
        [5,1,7,3],
        [6,2,8,4]
    ]
)

print('5x5 works: ',
    rot90(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ])
      
      ==
      
    [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5]
    ]
)