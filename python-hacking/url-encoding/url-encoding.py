import urllib.parse

# URL encoding
encoded = urllib.parse.quote('Hello World!')
print(encoded)  # Output: Hello%20World%21

# Double URL encoding
double_encoded = urllib.parse.quote(encoded)
print(double_encoded)  # Output: Hello%2520World%2521
