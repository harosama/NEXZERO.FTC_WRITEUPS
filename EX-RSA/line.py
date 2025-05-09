file_path = '/content/cList'

with open(file_path, 'r') as file:
    lines = [line.strip() for line in file]

# Print line 1443
print("Line 1443:", lines[1443])