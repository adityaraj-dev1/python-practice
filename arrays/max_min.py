arr = [7, 2, 9, 4, 1]

largest = arr[0]
smallest = arr[0]

for x in arr:
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x

print("Largest:", largest)
print("Smallest:", smallest)
