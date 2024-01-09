#include <string.h>

#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

string arr[64];
int n;
int cnt = 0;

bool IsSimple(int size, int x, int y) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (arr[x + i][y + j] != arr[x][y]) return false;
        }
    }

    return true;
}

void Sol(int size, int x, int y) {
    bool isSimple = true;
    if (size == 1) {  // 1 x 1이 되었을 경우 해당 숫자 return
        cout << arr[x][y];
        return;
    } else {                         // n x n 사이즈의 경우
        if (IsSimple(size, x, y)) {  // 모든 칸이 하나의 숫자로 이루어져있을 경우 해당 숫자 return
            cout << arr[x][y];
            return;
        } else {
            cout << "(";
            Sol(size / 2, x, y);
            Sol(size / 2, x, y + size / 2);
            Sol(size / 2, x + size / 2, y);
            Sol(size / 2, x + size / 2, y + size / 2);
            cout << ")";
            return;
        }
    }
}

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Sol(n, 0, 0);

    return 0;
}