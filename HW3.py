#Sarai Ayon
#4/22/2024
#CS240 Data Structures & Algorithms
# Algorithms HW 3 : Recursion vs Iteration

def binary_search_recursive(arr, target, start=0, end=None, operations=0):
    if end is None:
        end = len(arr) - 1

    if start > end:
        return -1, operations  # Target not found

    mid = (start + end) // 2
    operations += 1  # Count the operation

    if arr[mid] == target:
        return mid, operations  # Target found
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, start, mid - 1, operations)
    else:
        return binary_search_recursive(arr, target, mid + 1, end, operations)


# The file path where the numbers are stored
numbers_file = "C:\\Users\\Sarai Ayon\\OneDrive - Whatcom Community College\\Spring 2024\\CS240 Database Structure & Algorithms\\Week 3 Recursion vs Iteration\\numbers-3.txt"

# Open the file and read the numbers into a list
with open(numbers_file, 'r') as file:
    numbers = [int(line.strip()) for line in file]

# The number we want to search for
target = 5842193
# Call the binary_search function to find the position of the target in the array
position, num_operations = binary_search_recursive(numbers, target)
# Print the result
print(f"Position of {target} in the file: {position}")
print(f"Number of operations: {num_operations}")
