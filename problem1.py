import heapq

def merge_k_sorted_arrays(arrays):
    min_heap = []
    
    # Insert the first element of each array along with index details
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))
    
    result = []
    
    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)
        
        # Push the next element from the same array if exists
        if elem_idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(min_heap, (arrays[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1))
    
    return result

# Example Usage
arrays = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
print(merge_k_sorted_arrays(arrays))
