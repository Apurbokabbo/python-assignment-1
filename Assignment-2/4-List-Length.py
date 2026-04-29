def list_length(lst):
    count = 0
    for i in lst:
        count += 1
    return count

# Example usage
lists = [
    [1, 2, 3, 4, 5],
    ["a", "b", "c"],
    [],
    [True, 3.14, "hello", None, [1, 2]],
]

for l in lists:
    print(f"{l} -> Length: {list_length(l)}")