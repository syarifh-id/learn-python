import hashlib

def calculate_md5(file_path):
    try:
        with open(file_path, 'rb') as file:
            md5_hash = hashlib.md5()
            while chunk := file.read(8192):
                md5_hash.update(chunk)
            return md5_hash.hexdigest()
    except FileNotFoundError:
        return None

def validate_md5(file_path, expected_md5):
    actual_md5 = calculate_md5(file_path)
    if actual_md5:
        if actual_md5 == expected_md5:
            print(f"MD5 validation successful. File integrity is intact.")
        else:
            print(f"MD5 validation failed. The calculated MD5 ({actual_md5}) does not match the expected MD5 ({expected_md5}).")
    else:
        print(f"File not found: {file_path}")

# Example usage:
if __name__ == "__main__":
    file_path = "path/to/your/file.txt"
    expected_md5 = "your_expected_md5_here"
    validate_md5(file_path, expected_md5)

