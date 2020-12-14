#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int N;
	vector<int> num(5);
	cin >> N;
	for (int i=0; i < N; i++) {
		cin >> num[i];
	}

	for (int i = 0; i < N; i++) {
		for (int j = N-1; j >i; j--) {
			if (num[j-1]>num[j]) {
				int tmp = num[j];
				num[j] = num[j - 1];
				num[j - 1] = tmp;
			}
		}
	}

	for (int i=0; i < N; i++) {
		cout << num[i] << endl;
	}
}
///////////////////Bubble sort 개선!/////////////////////////////////////////
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int N;
	cin >> N;
	int arr[1000];
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	int k = 0;
	while (k < N-1) {
		//바뀐게 없는 경우 last가 N-1이 되어 바로 탈출
		int last = N - 1;
		for (int j = N - 1; j > k; j--) {
			if (arr[j - 1] > arr[j]) {
				//arr[j],arr[j-1] 'swap'
				int tmp = arr[j];
				arr[j] = arr[j - 1];
				arr[j - 1] = tmp;
				//last에 j를 계속 저장한다.
				//바뀔때마다 더 작은 j가 last에 저장되게 됨.
				last = j;
			}
		}
		k = last;
	}

	for (int i = 0; i < N; i++) {
		cout << arr[i] << "\n";
	}

	return 0;
}



//////////////vector 사용시 메모리 초과 발생 >> arr 사용 /////////////////////
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int N;
	cin >> N;
	int arr[1000];
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < N-1; i++) {
		for (int j = N - 1; j > i; j--) {
			if (arr[j - 1] > arr[j]) {
				int tmp = arr[j];
				arr[j] = arr[j - 1];
				arr[j - 1] = tmp;
			}
		}
	}

	for (int i = 0; i < N; i++) {
		cout << arr[i] << "\n";
	}

	return 0;
}

