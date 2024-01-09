<<<<<<< HEAD:jHyuk/week2/가장 긴 증가하는 수열.cpp
#include <string.h>

#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main() {
    vector<int> v;
    vector<int> maxCnt;

    int n, in, max;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> in;
        v.push_back(in);
    }

    for (int i = 0; i < n; i++) {
        max = 0;
        for (int j = 0; j < i; j++) {
            if (v[i] > v[j]) {
                if (max < maxCnt[j]) max = maxCnt[j];
            }
        }
        maxCnt.push_back(max + 1);
    }

    cout << *max_element(maxCnt.begin(), maxCnt.end());

    return 0;
=======
#include <string.h>

#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main() {
    vector<int> v;
    vector<int> maxCnt;

    int n, in, max;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> in;
        v.push_back(in);
    }

    for (int i = 0; i < n; i++) {
        max = 0;
        for (int j = 0; j < i; j++) {
            if (v[i] > v[j]) {
                if (max < maxCnt[j]) max = maxCnt[j];
            }
        }
        maxCnt.push_back(max + 1);
    }

    cout << *max_element(maxCnt.begin(), maxCnt.end());

    return 0;
>>>>>>> 108577b2c3c6646454d164e1559865e78d5d13da:jHyuk/2주차/가장 긴 증가하는 수열.cpp
}