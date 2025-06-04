# For LOOP
for i in range(1, 11, 3):
    print(i)

# FOR ELSE LOOP
successful = False
for i in range(3):
    print("Attempt")
    if successful:
        print(successful)
        break
else:  # else works if the loop fails to break or runs All iterations
    print("Attempted 3 times and Failed")

# Nested
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")
