import re

# Regex pattern
pattern = r'([\d\w]+)'

# Test string
test_string = "abc 123 xyz_456"

# Find all matches
matches = re.findall(pattern, test_string)

print(matches)  # Output: ['abc', '123', 'xyz_456']


# make regex
