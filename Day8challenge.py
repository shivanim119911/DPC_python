def reverseWords(s: str) -> str:
    # Step 1: Split words by spaces (this automatically removes extra spaces)
    words = s.split()
    
    # Step 2: Reverse the list of words
    reversed_words = words[::-1]
    
    # Step 3: Join them with a single space
    return " ".join(reversed_words)


# Example usage
s = "  the   sky  is   blue  "
print(reverseWords(s))  # Output: "blue is sky the"