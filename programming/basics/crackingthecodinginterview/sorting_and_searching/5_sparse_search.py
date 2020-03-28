import warnings

def search(arr: [str], s: str, l: int, r: int) -> int:
    while l <= r:
        m = (l + r) // 2
        if arr[m] == s:
            return m
        
        if m == l:
            return r if arr[r] == s else -1
        
        if len(arr[r]) > 0 and len(arr[l]) > 0 and (s > arr[r] or s < arr[l]):
            return -1

        if len(arr[m]) > 0:      
            if s > arr[m]:
                l = m + 1
            else:
                r = m - 1
        else:
            i = 1
            idx = m + i
            while idx <= r:
                if arr[idx] == s:
                    return idx
                
                if len(arr[idx]) > 0:
                    if arr[idx] < s:
                        l = idx + 1
                        m = (l + r) // 2
                    else:
                        r = idx - 1
                    break
                    
                i *= 2
                idx = m + i

            i = 1
            idx = m - i
            while idx >= l:
                if arr[idx] == s:
                    return idx
                
                if len(arr[idx]) > 0:
                    if arr[idx] > s:
                        r = idx - 1
                    else:
                        l = idx + 1
                    
                    break

                i *= 2
                idx = m - i
            
    return -1

if __name__ == "__main__":
    arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print(search(arr, "ball", 0, len(arr) - 1))
    print(search(arr, "at", 0, len(arr) - 1))
    print(search(arr, "car", 0, len(arr) - 1))
    print(search(arr, "dad", 0, len(arr) - 1))
    print(search(arr, "kancut", 0, len(arr) - 1))
