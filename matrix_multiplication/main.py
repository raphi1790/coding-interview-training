def multiply_matrices(mat_a,mat_b):
    if len(mat_a)==0 or len(mat_a[0])==0 or len(mat_b)==0 or len(mat_b[0]) == 0:
        return None
    a_rows = len(mat_a)
    a_cols = len(mat_a[0])
    b_rows = len(mat_b)
    b_cols = len(mat_b[0])
    if a_cols != b_rows:
        return None
    result = [[0 for i in range(b_cols)] for j in range(a_rows) ]
    for a_idx in range(a_rows):
        for b_idx in range(b_cols):
            element_res = 0
            for idx in range(a_cols):
                element_res += mat_a[a_idx][idx]*mat_b[idx][b_idx]
            result[a_idx][b_idx] = element_res
    return result

if __name__ == "__main__":
    mat_a = [[1,2,3],[4,5,6]]
    mat_b = [[5,6],[3,4],[1,2]]
    print(multiply_matrices(mat_a, mat_b))