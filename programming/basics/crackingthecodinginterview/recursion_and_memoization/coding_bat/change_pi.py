def change_pi(s: str):
    if len(s) < 2:
        return s
    
    arr = [s[0]]
    if s[:2] == "pi":
        arr[0] = "3.14"
        arr.append(change_pi(s[2:]))
    else:
        arr.append(change_pi(s[1:]))
    
    return "".join(arr)

if __name__ == "__main__":
    print(change_pi("xpix"))
    print(change_pi("pipi"))
    print(change_pi("pip"))

'''
public String changePi(String str) {
  if (str.length() < 2)
    return str;
  
  StringBuilder strBuilder = new StringBuilder();
  if (str.substring(0, 2).compareTo("pi") == 0) {
    strBuilder.append("3.14");
    strBuilder.append(changePi(str.substring(2)));
  } else {
    strBuilder.append(str.substring(0, 1));
    strBuilder.append(changePi(str.substring(1)));
  }
  
  return strBuilder.toString();
}
'''