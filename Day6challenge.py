def find_zero_sum_subarrays(arr):
    n = len(arr)
    result = []

    # prefix sum + hashmap to track indices
    prefix_sum = 0
    seen = {0: [-1]}  # prefix sum 0 seen before index -1

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum in seen:
            for start in seen[prefix_sum]:
                result.append((start + 1, i))

        seen.setdefault(prefix_sum, []).append(i)

    return result


# Example
arr = [1, 2, -3, 3, -1, 2]
print(find_zero_sum_subarrays(arr))