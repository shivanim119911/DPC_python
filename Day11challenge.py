from itertools import permutations


def string_permutations(s):
    # Generate all permutations using itertools
    perms = permutations(s)

    # Convert tuples to strings and remove duplicates using set
    unique_perms = set("".join(p) for p in perms)

    # Return as a sorted list (optional, for consistency)
    return sorted(unique_perms)


# Example
print(string_permutations("abc"))
