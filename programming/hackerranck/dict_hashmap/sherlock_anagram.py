# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen
import collections

def __is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    if collections.Counter(s1) == collections.Counter(s2):
        return True
    
    return False

def __anagram_counter(s1, s2):
    s1_len = len(s1)
    ctr = 0
    for i in range(len(s2)):
        a = __is_anagram(s1, s2[i:i+s1_len])
        #print("        __anagram counter: %s - %s -> %d" % (s1, s2[i:i+s1_len], a))
        if a:
            ctr += 1
    return ctr

def sherlockAndAnagrams(s):
    s_len = len(s)
    ctr = 0
    for i in range(1, s_len + 1):
        for j in range(s_len - i):
            #print(s[j:j+i] + " - " + s[j+1:])
            c = __anagram_counter(s[j:j+i], s[j+1:])
            #print(" anagram: %d" % c)
            ctr += c
    
    return ctr

assert sherlockAndAnagrams("abba") == 4
assert sherlockAndAnagrams("mom") == 2
assert sherlockAndAnagrams("abcd") == 0
assert sherlockAndAnagrams("ifailuhkqq") == 3
assert sherlockAndAnagrams("kkkk") == 10
assert sherlockAndAnagrams("cdcd") == 5
