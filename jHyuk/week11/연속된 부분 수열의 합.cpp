#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    vector<int> answer;
    vector<int> psum(sequence.size() + 1);

    int s = 0, e = 1;
    int min = 1000001;

    psum[0] = 0;

    for (int i = 0; i < sequence.size(); i++) {
        psum[i + 1] = psum[i] + sequence[i];
    }

    while (e < sequence.size() + 1 && s <= e) {
        if (psum[e] - psum[s] < k) {
            e++;
        }
        else if (psum[e] - psum[s] > k) {
            s++;
        }
        else {
            if (min > e - s) {
                answer.clear();
                answer.push_back(s);
                answer.push_back(e - 1);
                min = e - s;
            }
            e++;
        }
    }

    return answer;
}