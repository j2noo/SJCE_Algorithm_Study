#include <iostream>
#include <string.h>
using namespace std;

int main() {
	char str[101];
	int len;

	cin >> str;

	len = strlen(str);

	for (int i = 0; i < len / 2; i++) {
		if (str[i] != str[len - 1 - i]) {
			cout << 0;
			return 0;
		}
	}

	cout << 1;
	return 0;
}