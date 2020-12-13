#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	int N, h ,v;
	cin >> h >> v;
	cin >> N;
	vector<int> ver, hor;
	hor.push_back(0);
	ver.push_back(0);

	for (int i = 0; i < N; i++) {
		int a, b;
		cin >> a >> b;
		if (a == 0) {
			hor.push_back(b);
		}
		else {
			ver.push_back(b);
		}
	}
	hor.push_back(v);
	ver.push_back(h);
	sort(hor.begin(), hor.end());
	sort(ver.begin(), ver.end());

	int m_h=0, m_v=0;

	for (int i = 1; i < hor.size(); i++) {
		if (m_h < hor[i] - hor[i - 1]) {
			m_h = hor[i] - hor[i - 1];
		}
	}
	for (int i = 1; i < ver.size(); i++) {
		if (m_v < ver[i] - ver[i - 1]) {
			m_v = ver[i] - ver[i - 1];
		}
	}
	cout << m_v * m_h;

	return 0;
}