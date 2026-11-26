def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    if mode == 'column':
        i = 0
        val = 0
        while val < len(matrix[0]):
            tot = 0
            for j in range(len(matrix)):
                tot = tot + matrix[j][val]
            val += 1
            means.append(tot/len(matrix))
        return means
    elif mode == 'row':
        for row in matrix:
            tot = 0
            for i in row:
                tot = tot + i
            means.append(tot/len(matrix[0]))    
    return means