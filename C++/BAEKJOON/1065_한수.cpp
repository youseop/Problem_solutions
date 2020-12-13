#include<iostream>
using namespace std;

int arr[100001] = { 0,1,0, };

int main() {
	int n,cnt=0;
	cin >> n;
	if (n < 100) {
		cout << n;
	}
	else {
		cnt += 99;
		for (int i = 100; i <= n; i++) {
			int a = i % 10;
			int b = (i / 10) % 10;
			int c = (i / 100);
			if (a - b == b - c) {
				cnt++;
			}
		}
		cout << cnt;
	}


	return 0;
}