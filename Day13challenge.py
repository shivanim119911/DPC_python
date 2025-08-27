def longestPalindrome(s: str) -> str:
    if not s or len(s) == 1:
        return s

    def expandAroundCenter(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome
        odd = expandAroundCenter(i, i)
        # Even-length palindrome
        even = expandAroundCenter(i, i + 1)

        # Update longest
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even

    return longest


# Example
print(longestPalindrome("babad"))  # "bab" or "aba"
print(longestPalindrome("cbbd"))  # "bb"
