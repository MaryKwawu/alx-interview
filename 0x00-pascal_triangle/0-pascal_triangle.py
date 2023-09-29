def pascal_triangle(n):
    # Check for invalid input
    if n <= 0:
        return []

    # Initialize the triangle with the first row containing 1
    triangle = [[1]]

    # Generate the triangle rows up to the nth row
    for i in range(1, n):
        # Calculate the current row based on the previous row
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1

        for j in range(1, i):
            new_element = prev_row[j - 1] + prev_row[j]
            new_row.append(new_element)

        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
    return triangle
