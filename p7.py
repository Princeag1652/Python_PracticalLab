# 1. Remove negative values using filter()
def remove_negative(matrix):
    return [
        list(filter(lambda x: x >= 0, row))
        for row in matrix
    ]


# 2. Sort each row using a custom key
def sort_rows(matrix, reverse=False):
    return [
        sorted(row, key=lambda x: x, reverse=reverse)
        for row in matrix
    ]


# 3. Flatten the matrix and sort all elements
def flatten_and_sort(matrix, reverse=False):
    flat_list = [x for row in matrix for x in row]
    return sorted(flat_list, reverse=reverse)


# 4. Add a constant to every element using map()
def add_constant(matrix, constant):
    return [
        list(map(lambda x: x + constant, row))
        for row in matrix
    ]


# 5. Transpose the matrix using zip()
def transpose_matrix(matrix):
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]


# Main program
if __name__ == "__main__":
    matrix = [
        [3, -2, 7, 0],
        [4, 5, -6, 8],
        [-1, 9, 2, -3],
        [6, -4, 5, 10]
    ]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    print("\nAfter removing negative values:")
    for row in remove_negative(matrix):
        print(row)

    print("\nAfter sorting each row (ascending):")
    for row in sort_rows(remove_negative(matrix)):
        print(row)

    print("\nFlattened and sorted elements (ascending):")
    print(flatten_and_sort(remove_negative(matrix)))

    print("\nAfter adding constant 5:")
    for row in add_constant(remove_negative(matrix), 5):
        print(row)

    print("\nTransposed Matrix:")
    for row in transpose_matrix(matrix):
        print(row)
