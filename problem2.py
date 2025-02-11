def remove_duplicates(arr):
    if not arr:
        return []
    
    write_index = 1  # Start writing from the second position
    for read_index in range(1, len(arr)):
        if arr[read_index] != arr[read_index - 1]:
            arr[write_index] = arr[read_index]
            write_index += 1
    
    return arr[:write_index]

# Example Usage
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(remove_duplicates(arr))
