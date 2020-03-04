def change_xy(s: str):
    if len(s) == 0:
        return ""
    
    arr = [s[0]]
    if s[0] == "x":
        arr[0] = "y"
    
    arr.append(change_xy(s[1:]))
    return "".join(arr)

print(change_xy("xhixhix"))
