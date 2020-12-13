#include<iostream>
#include<math.h>
#include<string>
using namespace std;

void hanoi(int n, int f, int v, int t) {
	if (n == 1) {
		cout << f << ' ' << t << "\n";
	}
	else {
		hanoi(n - 1, f, t, v);
		cout << f << ' ' << t << "\n";
		hanoi(n - 1, v, f, t);
	}
}
int main() {
	int n;
	cin >> n;
	//cout << (1<<n)-1 << "\n";
	
	//옮긴 횟수 출력
	string s = to_string(pow(2, n));
	int i = s.find('.');
	s = s.substr(0, i);
	s[s.length() - 1] -= 1;
	cout << s<<"\n";

	if (n <= 20) {
		hanoi(n,1,2,3);
	}
	return 0;
}