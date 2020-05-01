#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.size() == 0)
            return 0;

        std::priority_queue<int, std::vector<int>, std::greater<int>> q;
        std::sort(intervals.begin(), intervals.end(), 
            [](const std::vector<int> &a, const std::vector<int> &b){
                return a.at(0) < b.at(0);
            });
        
        for (auto meeting : intervals) {
            int start = meeting.at(0);
            int end = meeting.at(1);
            if (q.empty()) {
                q.push(end);
            } else {
                if (start >= q.top()) {
                    q.pop();
                }
                q.push(end);
            }
        }

        return q.size();
    }
};

int main() {
    std::priority_queue<int, std::vector<int>, std::greater<int>> q;
 
    for(int n : {1,8,5,6,3,4,0,9,7,2})
        q.push(n);
 
    while (!q.empty()) {
        std::cout << q.top() << ", ";
        q.pop();
    }

    return 0;
}