'''
https://codingbat.com/prob/p184029

Given a string, compute recursively (no loops) the number of times lowercase 
"hi" appears in the string.

countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1

public int countHi(String str) {
  if (str.length() < 2) 
    return 0;
  
  int total = 0;
  if (str.substring(0, 2).compareTo("hi") == 0) {
    total = 1;
  }
  
  return total + countHi(str.substring(1));
}

'''