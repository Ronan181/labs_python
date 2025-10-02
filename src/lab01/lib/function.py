def same_len(matrix):
    for el_matrix in matrix:
        if len(el_matrix)!=len(matrix[0]):
            raise ValueError
        else:
            return matrix
