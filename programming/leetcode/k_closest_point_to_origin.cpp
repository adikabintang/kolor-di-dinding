// https://leetcode.com/problems/k-closest-points-to-origin/submissions/
// Runtime: 388 ms, faster than 44.33% of C++ online submissions
// Memory Usage: 34.4 MB, less than 100.00% of C++ online submissions
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        std::sort(points.begin(), points.end(),
                 [](const std::vector<int> &a, const std::vector<int> &b){
                     return (a[0] * a[0] + a[1] * a[1]) < 
                         (b[0] * b[0] + b[1] * b[1]);
                 });
        return std::vector< std::vector<int> >(points.begin(), points.begin() + K);
    }
};
