#include <math.h>
#include <string.h>

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int FindMin(char A[10]) {
    int ret;

    for (int i = 0; i < 10; i++) {
        if (A[i] == '6') {
            A[i] = '5';
        }
    }

    ret = atoi(A);

    return ret;
}

int FindMax(char A[10]) {
    int ret;

    for (int i = 0; i < 10; i++) {
        if (A[i] == '5') {
            A[i] = '6';
        }
    }

    ret = atoi(A);

    return ret;
}

int main() {
    char A[10], B[10];

    cin >> A >> B;

    cout << FindMin(A) + FindMin(B) << ' ' << FindMax(A) + FindMax(B);

    return 0;
}