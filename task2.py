def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        for column in range(1, num_columns + 1):
            element = operation(row, column)
            print(element, end='\t')
        print()

def multiply(row, column):
    return row * column

print_operation_table(multiply, num_rows=6, num_columns=6)
