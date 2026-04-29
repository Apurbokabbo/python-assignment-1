d = {"banana": 3, "apple": 1, "cherry": 2}

sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))

print(sorted_d)