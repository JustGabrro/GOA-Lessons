def find_value(a, v):
    # Iterate through the list a
    for i in range(len(a)):
        if a[i] == v:  # Check if the current element is equal to v
            print(f"Found value in place {i}.")
            return 0  # Return 0 to indicate success
    print("Value not found.")
    return 1  # Return 1 to indicate failure