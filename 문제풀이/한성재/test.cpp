/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// float b, c;
// double d, e, f;
// char g;
// char var[256];
// long long AB;
// scanf("%d", &a);                      // int 변수 1개 입력받는 예제
// scanf("%f %f", &b, &c);               // float 변수 2개 입력받는 예제 
// scanf("%lf %lf %lf", &d, &e, &f);     // double 변수 3개 입력받는 예제
// scanf("%c", &g);                      // char 변수 1개 입력받는 예제
// scanf("%s", &var);                    // 문자열 1개 입력받는 예제
// scanf("%lld", &AB);                   // long long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// float b = 1.0, c = 2.0;               
// double d = 3.0, e = 0.0; f = 1.0;
// char g = 'b';
// char var[256] = "ABCDEFG";
// long long AB = 12345678901234567L;
// printf("%d", a);                      // int 변수 1개 출력하는 예제
// printf("%f %f", b, c);                // float 변수 2개 출력하는 예제
// printf("%lf %lf %lf", d, e, f);       // double 변수 3개 출력하는 예제
// printf("%c", g);                      // char 변수 1개 출력하는 예제
// printf("%s", var);                    // 문자열 1개 출력하는 예제
// printf("%lld", AB);                   // long long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int map[101][101];
bool visited[101][101] = {false};
int a_dir[2] = {0,1};
int b_dir[2] = {1,0};
queue<pair<int,int>> q;

void doBfs(int stage, int init_a, int init_b){
    visited[init_a][init_b] = true;
    q.push(make_pair(init_a,init_b));
    
    while (!q.empty()){

        int a = q.front().first;
        int b = q.front().second;

        q.pop();

        for(int i=0; i<2; i++){
            int a_new = a + a_dir[i];
            int b_new = b + b_dir[i];

            if(!visited[a_new][b_new]){
                if(map[a_new][b_new] > stage){
                    visited[a_new][b_new] = true;
                    q.push(make_pair(a_new,b_new));
                }
            }

            
        }
    }
    
}

int main(void){
	int test_case;
	int T;

	/* 아래의 freopen 함수는 input.txt 를 read only 형식으로 연 후,
	앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
	여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
	freopen 함수를 이용하면 이후 scanf 를 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
	따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 함수를 사용하셔도 좋습니다.
	단, 채점을 위해 코드를 제출하실 때에는 반드시 freopen 함수를 지우거나 주석 처리 하셔야 합니다.
	*/
	// freopen("input.txt", "r", stdin);
	/* 아래 코드를 수행하지 않으면 여러분의 프로그램이 제한 시간 초과로 강제 종료 되었을 때,
	출력한 내용이 실제 표준 출력에 기록되지 않을 수 있습니다.
	따라서 안전을 위해 반드시 setbuf(stdout, NULL); 을 수행하시기 바랍니다.
	*/
	setbuf(stdout, NULL);
	scanf("%d", &T);
	/*
	여러 개의 테스트 케이스를 처리하기 위한 부분입니다.
	*/
	for (test_case = 1; test_case <= T; ++test_case){
        fill(&visited[0][0], &visited[101 - 1][101], false);
        int N;
        int sectorNum;
        int max_sectorNum = -1;
        cin >> N;
        for(int i = 0; i< N; i++){
            for (int k=0; k<N; k++){
                cin >> map[i][k];
            }
        }

        //한단계씩 늘려가며 bfs 매 단계 마다 땅 개수 max 최신화, 이후, 최댓값 print
        for(int stage = 1; stage<101; stage++){
            sectorNum = 0;
            for (int i=0; i<N; i++ ){
                for(int k=0; k<N; k++){
                    //1. visited에 없고, 2. 높이보다 크면(초과) bfs 실행
                    if(!visited[i][k] && map[i][k] > stage){
                        doBfs(stage,i,k);
                        sectorNum++;
                    }
                }
            }
            max_sectorNum = max(max_sectorNum,sectorNum);
        }
        cout << "\n" << "#" << test_case << " " << max_sectorNum;
	}
	return 0; //정상종료시 반드시 0을 리턴해야 합니다.
}