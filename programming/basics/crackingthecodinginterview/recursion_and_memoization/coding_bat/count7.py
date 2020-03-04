'''
https://codingbat.com/prob/p101409 

Given a non-negative int n, return the count of the occurrences of 7 as a digit, 
so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the 
rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost 
digit (126 / 10 is 12).

count7(717) → 2
count7(7) → 1
count7(123) → 0

public int count7(int n) {
  if (n == 0)
    return 0;
  
  int count = (n % 10 == 7 ? 1 : 0);
  return count + count7(n / 10);
}
'''