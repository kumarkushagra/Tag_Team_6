import os

# Input the full directory path
full_path = input("D/sample/last")

# Normalize the path to handle different separators and remove redundant separators
normalized_path = os.path.normpath(full_path)

# Split the path into components
components = normalized_path.split(os.sep)

# Print the bottom-most directory
bottom_most = components[-1]
print("Bottom-most directory:", bottom_most)