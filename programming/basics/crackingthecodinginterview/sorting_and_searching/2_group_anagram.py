arr = ["ot", "abc", "are", "bca", "era", "acb", "to"]
arr.sort(key=sorted)
print(arr)

# or
m = {}
for s in arr:
    key = "".join(sorted(s))
    if key not in m:
        m[key] = [s]
    else:
        m[key].append(s)    

result = []
for key, value in m.items():
    for e in value:
        result.append(e)

print(result)