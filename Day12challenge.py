def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:  # It's a closing bracket
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:  # It's an opening bracket
            stack.append(char)

    return not stack  # Valid if stack is empty


# Example
print(isValid("[{()}]"))  # Output: True
print(isValid("[{(}]"))  # Output: False
print(isValid("((()))"))  # Output: True
