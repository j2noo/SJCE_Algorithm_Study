#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int>& v1, vector<int>& v2) {
    if (v1[1] == v2[1])
        return v1[0] < v2[0];
    else return v1[1] < v2[1];
}

int solution(vector<vector<int>> targets) {
    int answer = 0;
    int idx = 0;
    sort(targets.begin(), targets.end(), cmp);

    for (int i = 0; i < targets.size(); i++) {
        if (targets[i][0] < idx) {
            continue;
        }
        else {
            idx = targets[i][1];
            answer++;
        }

    }

    return answer;
}