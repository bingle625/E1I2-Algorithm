/////////////////////////////////////////////////////////////////////////////////////////////
// �⺻ �����ڵ�� ���� �����ص� ���� �����ϴ�. ��, ����� ���� ����
// �Ʒ� ǥ�� ����� ���� �ʿ�� �����ϼ���.
// ǥ�� �Է� ����
// int a;
// float b, c;
// double d, e, f;
// char g;
// char var[256];
// long long AB;
// scanf("%d", &a);                      // int ���� 1�� �Է¹޴� ����
// scanf("%f %f", &b, &c);               // float ���� 2�� �Է¹޴� ���� 
// scanf("%lf %lf %lf", &d, &e, &f);     // double ���� 3�� �Է¹޴� ����
// scanf("%c", &g);                      // char ���� 1�� �Է¹޴� ����
// scanf("%s", &var);                    // ���ڿ� 1�� �Է¹޴� ����
// scanf("%lld", &AB);                   // long long ���� 1�� �Է¹޴� ����
/////////////////////////////////////////////////////////////////////////////////////////////
// ǥ�� ��� ����
// int a = 0;                            
// float b = 1.0, c = 2.0;               
// double d = 3.0, e = 0.0; f = 1.0;
// char g = 'b';
// char var[256] = "ABCDEFG";
// long long AB = 12345678901234567L;
// printf("%d", a);                      // int ���� 1�� ����ϴ� ����
// printf("%f %f", b, c);                // float ���� 2�� ����ϴ� ����
// printf("%lf %lf %lf", d, e, f);       // double ���� 3�� ����ϴ� ����
// printf("%c", g);                      // char ���� 1�� ����ϴ� ����
// printf("%s", var);                    // ���ڿ� 1�� ����ϴ� ����
// printf("%lld", AB);                   // long long ���� 1�� ����ϴ� ����
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

	/* �Ʒ��� freopen �Լ��� input.txt �� read only �������� �� ��,
	������ ǥ�� �Է�(Ű����) ��� input.txt ���Ϸκ��� �о���ڴٴ� �ǹ��� �ڵ��Դϴ�.
	�������� �ۼ��� �ڵ带 �׽�Ʈ �� ��, ���Ǹ� ���ؼ� input.txt�� �Է��� ������ ��,
	freopen �Լ��� �̿��ϸ� ���� scanf �� ������ �� ǥ�� �Է� ��� ���Ϸκ��� �Է��� �޾ƿ� �� �ֽ��ϴ�.
	���� �׽�Ʈ�� ������ ������ �Ʒ� �ּ��� ����� �� �Լ��� ����ϼŵ� �����ϴ�.
	��, ä���� ���� �ڵ带 �����Ͻ� ������ �ݵ�� freopen �Լ��� ����ų� �ּ� ó�� �ϼž� �մϴ�.
	*/
	// freopen("input.txt", "r", stdin);
	/* �Ʒ� �ڵ带 �������� ������ �������� ���α׷��� ���� �ð� �ʰ��� ���� ���� �Ǿ��� ��,
	����� ������ ���� ǥ�� ��¿� ��ϵ��� ���� �� �ֽ��ϴ�.
	���� ������ ���� �ݵ�� setbuf(stdout, NULL); �� �����Ͻñ� �ٶ��ϴ�.
	*/
	setbuf(stdout, NULL);
	scanf("%d", &T);
	/*
	���� ���� �׽�Ʈ ���̽��� ó���ϱ� ���� �κ��Դϴ�.
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

        //�Ѵܰ辿 �÷����� bfs �� �ܰ� ���� �� ���� max �ֽ�ȭ, ����, �ִ� print
        for(int stage = 1; stage<101; stage++){
            sectorNum = 0;
            for (int i=0; i<N; i++ ){
                for(int k=0; k<N; k++){
                    //1. visited�� ����, 2. ���̺��� ũ��(�ʰ�) bfs ����
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
	return 0; //��������� �ݵ�� 0�� �����ؾ� �մϴ�.
}