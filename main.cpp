#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

void print(vector<int> &A) {
    for (int i = 0; i < A.size(); i++) {
        std::cout << A.at(i) << " ";
    }
    std::cout << std::endl;
} 


unsigned int spike_len(vector<int> &A) {
    int prev_up = A.at(0);
    unsigned int i = 0, idx = 0, max_len = 0;
    
    while (idx < A.size()) {
        i = idx+1;
        while (i < A.size() && A.at(i) > prev_up) {
            prev_up = A.at(i);
            i++;
        }
        
        int prev_down = prev_up;
        i++;
        while (i < A.size() && A.at(i) < prev_down) {
            prev_down = A.at(i);
            i++;
        }
        if (prev_down < prev_up) {
            max_len = std::max(max_len, i - idx);
        }
        
        idx = i;
    }
    
    return max_len;
}

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    std::sort(A.begin(), A.end(), greater<int>());
    std::vector<int> clone = A;
    print(clone);
    unsigned int maxi = 0;
    for (unsigned int i = 0; i < A.size(); i++) {
        clone = A;
        std::cout << "oioioi" << std::endl;
        for (unsigned int j = i; j > 0; j--) {
            int temp = clone.at(j);
            clone.at(j) = clone.at(j - 1);
            clone.at(j - 1) = temp;
            print(clone);
            maxi = std::max(maxi, spike_len(clone));   
        }
        maxi = std::max(maxi, spike_len(clone));
        std::cout << "maxi: " << maxi << std::endl;
    }
    
    return maxi;
}

int main() {
    std::vector<int> a{2, 3, 3, 2, 2, 2, 1};
    int x = solution(a);
    //int x = spike_len(a);
    std::cout << std::endl << x << std::endl;
}