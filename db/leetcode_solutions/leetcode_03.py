def longest_substring_without_repeating_characters(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest substring without repeating characters.
    """

    longest_length = 0
    start = 0
    char_index = {}  # Store the last seen index of each character

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            # If the current character has been seen before and is within the current substring
            start = char_index[s[end]] + 1  
        
        char_index[s[end]] = end  # Update the last seen index of the current character
        longest_length = max(longest_length, end - start + 1)  

    return longest_length

# Example usage
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

print(f"Length of longest substring in '{s1}': {longest_substring_without_repeating_characters(s1)}")
print(f"Length of longest substring in '{s2}': {longest_substring_without_repeating_characters(s2)}")
print(f"Length of longest substring in '{s3}': {longest_substring_without_repeating_characters(s3)}")