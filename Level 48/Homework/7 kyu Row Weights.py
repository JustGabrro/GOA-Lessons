def row_weights(array):
    x = sum(array[i] for i in range(0, len(array), 2))
    x1 = sum(array[i] for i in range(1, len(array), 2))
    return (x, x1)