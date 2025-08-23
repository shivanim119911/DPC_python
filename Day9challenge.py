def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as the prefix
    prefix = strs[0]
    
    # Compare prefix with every other string
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]  # reduce prefix length by 1
            if not prefix:
                return ""
    return prefix


# Example usage
words = ["flower", "flow", "flight"]
print(longestCommonPrefix(words))  # Output: "fl"