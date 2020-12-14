#include<iostream>
#include<vector>
#include<string>
using namespace std;

int N = 0, answer = 0;

//퀸을 놓을 수 있는 칸을 한줄씩 탐색
//재귀함수로 한칸 더 깊이 들어가면 다음 줄로 이동했다는 의미이다.
void queen(int cnt, vector<int> left, vector<int> center, vector<int> right) {
    if (cnt == N) {
        //N개를 모두 배치했음으로 경우의 수에 1 추가
        answer++;
        return;
    }
    //좌하단 대각선 성분은 왼쪽으로 한 칸씩 밀어준다.
    for (int i = 1; i < N; i++) {
        left[i - 1] = left[i];
    }
    left[N - 1] = 0;
    //우하단 대각선 성분은 오른쪽으로 한 칸씩 밀어준다.
    for (int i = N-1; i >0 ; i--) {
        right[i] = right[i-1];
    }
    right[0] = 0;
    //left,right,center에 흩어진 정보를 combine에 합친다.
    vector<int> combine(N);
    for (int i = 0; i < N; i++) {
        if (left[i] || right[i] || center[i]) {
            combine[i] = 1;
        }
    }
    //해당 줄의 0부터 N칸까지 탐색하며 퀸을 배치한다.
    for (int i = 0; i < N; i++) {
        if (combine[i] == 0) {
            left[i] = 1;
            center[i] = 1;
            right[i] = 1;
            queen(cnt + 1, left, center, right);
            //이번 칸에 배치하지 않고 다음 칸에 배치하는 경우도 생각해야 함으로
            //다시 0으로 reset해준다.
            left[i] = 0;
            center[i] = 0;
            right[i] = 0;
        }
    }
}

int main()
{
    cin >> N;
    //vector원소가 0인 칸에만 queen배치 가능
    vector<int> left(N), center(N), right(N);
    queen(0, left, center, right);
    cout << answer;
}
