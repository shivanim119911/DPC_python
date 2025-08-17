def findDuplicate(arr):
    # Phase 1: Finding the intersection point
    slow = arr[0]
    fast = arr[0]

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    # Phase 2: Finding the entrance to the cycle (duplicate)
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow


# Example usage
arr = [3, 1, 3, 4, 2]
print("Duplicate number is:", findDuplicate(arr))