import numpy as np
# 1.7 Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.

# I would use numpy, since it is a matrix, but do as array since not
# doing linear algebra.

def matrix_zero(matrix):
    """ (array) -> array
    Check matrix for zeros. Any column or row with a 0 in it, causes that row
    or column to become all zeros. Return new matrix.

    >>> matrix_zero(np.array([[1,2,3],[0,1,3],[1,3,4]]))
    array([[0, 2, 3],
       [0, 0, 0],
       [0, 3, 4]])
    >>> matrix_zero(np.array([[0,0,0],[0,9,0],[1,0,0]]))
    array([[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]])
     >>> matrix_zero(np.array([[1,2,3],[2,5,3],[1,3,4]]))
    ([1 2 3; 2 5 3; 1 3 4])
    """
    # I want to use lists so I can get the index for the row
    # but I want to use arrays so I can change entire columns or rows
    # Argh! This would be easier in Matlab, I wouldn't even have to loop
    
    new_matrix = matrix.copy()
    # go through rows
    for i in range(0,len(matrix)):
        # go through each number in row, find zeros
        for j, yval in enumerate(matrix[i,:]):
            if (yval== 0):
                # if you find a zero,make that column and row all zeros
                new_matrix[:,j] = 0;
                new_matrix[i,:] = 0;
    return new_matrix

