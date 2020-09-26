"""
In linear algebra, the transpose of a matrix is another matrix created by writing the
rows of as the columns of , for example:
Write a function transpose that transposes a matrix, for example:
transpose( [ [1,2], [3,4] ] ) # returns [ [1,3], [2,4] ]
transpose( [ [1,2,3,4], [5,6,7,8] ] ) # returns [ [1,5], [2,6], [3,7], [4,8] ]

"""


def transpose(matrix):
    matrix_transpose = []
    # Loop through columns on outside loop
    for c in range(len(matrix[0])):
        new_row = []
        # Loop through columns on inner loop
        for r in range(len(matrix)):
            # Column values will be filled by what were each row before
            new_row.append(matrix[r][c])
        matrix_transpose.append(new_row)

    return matrix_transpose


print("Problem 6 Solution")
print(transpose( [ [1,2], [3,4] ] ))
print(transpose( [ [1,2,3,4], [5,6,7,8] ] ))

##Additional check
assert  transpose( [ [1,2], [3,4] ] ) == [ [1,3], [2,4] ] , "Check transpose case1"
assert transpose( [ [1,2,3,4], [5,6,7,8] ])  == [ [1,5], [2,6], [3,7], [4,8] ], "Check transpose case2"