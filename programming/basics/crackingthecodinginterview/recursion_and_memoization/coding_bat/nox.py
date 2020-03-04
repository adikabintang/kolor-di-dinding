def nox(s: str):
    if len(s) == 0:
        return ""
    
    arr = []
    if s[0] != "x":
        arr.append(s[0])
    
    arr.append(nox(s[1:]))
    return "".join(arr)

if __name__ == "__main__":
    print(nox("xaxb"))
    print(nox("xx"))

'''
public String noX(String str) {
  if (str.length() == 0) {
    return "";
  }
  
  StringBuilder strBuilder = new StringBuilder();
  if (str.substring(0, 1).compareTo("x") != 0) {
    strBuilder.append(str.substring(0, 1));
  }
  
  strBuilder.append(noX(str.substring(1)));
  
  return strBuilder.toString();
}
'''