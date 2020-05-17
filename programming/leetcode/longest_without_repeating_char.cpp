/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * Runtime: 60 ms, faster than 25.12% of C++ online submissions
 * Memory Usage: 11 MB, less than 52.24% of C++ online submissions
 * remember: sliding window
 */
#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxi = 0;
        std::unordered_set<char> uniq;
        int i = 0, j = 0;
        while (i < s.length()) {
            while (j < s.length() && uniq.find(s[j]) == uniq.end()) {
                uniq.insert(s[j++]);
            }
            if (uniq.size() > maxi) {
                maxi = uniq.size();
            }
            if (uniq.find(s[j - 1]) != uniq.end()) {
                uniq.erase(s[i++]);
            }
        }
        return maxi;
    }
};

int main()
{
    Solution s;
    std::cout << s.lengthOfLongestSubstring("abcda") << endl;
    return 0;
}