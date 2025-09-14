// 아기상어

// N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 
// 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 
// 한 칸에는 물고기가 최대 1마리 존재한다.

// 아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 
// 가장 처음에 아기 상어의 크기는 2이고, 
// 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

// 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 
// 나머지 칸은 모두 지나갈 수 있다. 
// 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
// 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

// 아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

//[이동 조건]
// 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.(도움요청 => 종료)
// 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
// 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
// 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
// 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.

// 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 
// 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 
// 물고기를 먹으면, 그 칸은 빈 칸이 된다.

// 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 
// 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

// 공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

// [입력값]
// 첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.
// 둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.
// 0: 빈 칸
// 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
// 9: 아기 상어의 위치
// 아기 상어는 공간에 한 마리 있다.

// [출력값]
// 첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.

// [고민]
// 20 * 20이라 콜스택 넘기는데
// 재귀 말고 큐를 사용해야 할 듯
// 현재 위치에서 가장 가까운 물고기 위치를 구할때 본인보다 큰 물고기가 가로막는 경우를 고려해야 하는지? => 고려한다면 거리계산을 어떻게 해야하지?
// 여기서 BFS를 사용해서 최단거리를 구하면 시간복잡도는 괜찮을까?
// 시간복잡도는 20 * 20 = 400인 칸에서 진행한다고 생각했을때 시간초과가 생기진 않을거 같은데..?
// 물고기 거리가 등록됐을때 그 최단거리를 넘어선 배열은 가지치기 하고(최단거리라 가능하네)

// [문제 풀이]
// 상어의 처음 크기는 2임
// 우선 배열을 전부 탐색해서 아기상어의 시작점을 찾으면 [아기상어 이동시간 구하기 함수]를 실행해서 총 시간을 구한다.

// [아기상어 이동시간 구하기 함수]
// 큐를 사용해서 반복문을 실행함
// 큐에 들어갈 값 => [아기상어 좌표(x, y), 아기상어 크기, 아기상어 성장까지 더 먹어야 하는 물고기 수]
// 먹을 수 있는 가장 가까운 물고기를 구하기 위해 [최단 경로 물고기 구하기 BFS]를 사용한다.

// [최단 경로 물고기 구하기 BFS]
// 큐에 담을 값 => [아기상어 좌표, 아기상어 크기, 이동 횟수]
// visited 필요
// 현재까지의 최단 경로 변수 필요
// 상어와 왼쪽 거리 차이 담을 변수 필요
// 물고기의 좌표를 담을 변수 필요
// 현재 좌표로 4방향 탐색을 시작함
// 범위를 벗어나지 않고, 방문하지 않았고, 본인보다 큰 물고기가 없는 지역으로 이동
// 본인보다 작은 물고기를 발견하면 최단경로값을 비교해보고, 
// 더 짧은 경로라면 최단경로, 물고기 좌표를 업데이트
// 경로값이 같다면 
// - 물고기의 y좌표가 더 작은(더 위에 위치하는) 물고기의 물고기 좌표를 업데이트
// y 좌표도 같다면
// - 물고기의 x좌표가 더 작은(더 왼쪽에 위치하는) 물고기의 물고기 좌표를 업데이트
// 그 외에 이동 횟수가 최단경로보다 큰 경우엔 이동중단하기
// 최종적으로 최단 거리, 물고기 좌표를 반환(아무것도 못 찾았으면 -1)

// [최단 경로 물고기 구하기 BFS]가 종료되었을때 물고기 좌표가 구해지지 않았다면(-1, -1)
// 아기상어보다 큰 물고기들 때문에 이동할 수 없는 상태이기 때문에 결과 반환하고 [아기상어 이동시간 구하기 함수] 종료

// 가장 가까운 물고기 좌표를 구했으면
// 총 이동거리에 최단거리를 더해주고, 현재 상어의 위치를 물고기 좌표로 이동시키고, 아기상어 성장까지 더 먹어야 하는 물고기 수에 +1 해주고, 해당 좌표값을 0으로 교체한다.
// 그리고 아기상어 크기만큼 물고기를 먹었다면 아기상어 크기를 +1 해주고, 아기상어 성장까지 더 먹어야 하는 물고기 수를 0으로 바꿔준다.

// 이제 함수를 무한반복해서 [아기상어 이동시간 구하기 함수]가 종료되었을때의 결과값을 반환하면 끝

import java.io.*;
import java.util.*;

class Main {
    static int N;
    static int[][] ocean;
    // 델타
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    // [아기상어 이동시간 구하기 함수]
    // 상어 x좌표, 상어 y좌표, 상어 크기, 상어 경험치
    static int baby_shark_move(int x, int y, int size, int exp){
        // 덱 생성
        Deque<int[]> deq = new ArrayDeque<>();
        // 초기값 담기
        deq.addFirst(new int[] {x, y, size, exp});
        // 총 이동시간(경로)
        int total_path = 0;

        while(!deq.isEmpty()){
            // 현재 물고기 정보 빼기
            int[] cur = deq.pollFirst();
            int shark_x = cur[0];
            int shark_y = cur[1];
            int shark_size = cur[2];
            int shark_exp = cur[3];

            // 물고기 최단 경로 구하기
            int[] minimun_fish_path_res = minimum_fish_path(shark_x, shark_y, shark_size);
            int fish_x = minimun_fish_path_res[0];
            int fish_y = minimun_fish_path_res[1];
            int minimum_path = minimun_fish_path_res[2];

            // 물고기가 없는 경우(-1, -1) 바로 total_path 반환하고 종료
            if(fish_x == -1 && fish_y == -1){
                return total_path;
            // 물고기가 있는 경우
            } else {
                // 현재 위치 물고기 잡아먹기
                ocean[fish_y][fish_x] = 0;
                // 총 이동 횟수에 경로 추가
                total_path += minimum_path;
                // 현재 exp가 shark_size만큼 달성했으면 exp 초기화, 물고기 키워서 넘기기
                if(shark_exp + 1 == shark_size){
                    deq.addLast(new int[] {fish_x, fish_y, shark_size + 1, 0});
                } else {
                    deq.addLast(new int[] {fish_x, fish_y, shark_size, shark_exp + 1});
                }
            }
        }

        // 결과 반환
        return total_path;
    }

    // [최단 경로 물고기 구하기 BFS]
    static int[] minimum_fish_path(int shark_x, int shark_y, int shark_size){
        // 덱 생성
        Deque<int[]> deq = new ArrayDeque<>();
        deq.addFirst(new int[] {shark_x, shark_y, 0});

        // 방문여부 초기화
        boolean[][] visited = new boolean[N][N];
        for(int y = 0; y < N; y++){
            for(int x = 0; x < N; x++){
                visited[y][x] = false;
            }
        }
        // 시작 위치 체크
        visited[shark_y][shark_x] = true;

        // 물고기 최단 경로(최대는 아마 401 정도지 않을까)
        int minimum_path = 401;
        // 물고기 x, y 좌표
        int fish_x = -1;
        int fish_y = -1;

        while(!deq.isEmpty()){
            int[] cur = deq.pollFirst();
            int x = cur[0];
            int y = cur[1];
            int path = cur[2];
            // 현재 위치에 아기상어보다 작은 물고기가 있으면
            if(ocean[y][x] > 0 && shark_size > ocean[y][x]){
                // 현재 경로가 더 짧으면 업데이트
                if(minimum_path > path){
                    minimum_path = path;
                    fish_x = x;
                    fish_y = y;
                }
                // 경로 길이가 같으면
                else if(minimum_path == path){
                    // 위로 가장 멀리 있는 물고기 선택
                    if(fish_y > y){
                        fish_x = x;
                        fish_y = y;
                    }
                    // 위가 똑같다면
                    else if(fish_y == y){
                        // 왼쪽으로 가장 멀리 있는 물고기 선택
                        if(fish_x > x){
                            fish_x = x;
                            fish_y = y;
                        }
                    }
                }
            }

            // 다음 지역 이동
            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                // 이동 가능 여부 검증(다음 이동횟수가 minimum_path 넘어가지 않았고, 범위 벗어나지 않고, 방문하지 않았고, 아기상어 보다 큰 물고기가 없는 경우)
                if(nx >= 0 && ny >= 0 && nx < N && ny < N && !visited[ny][nx] && ocean[ny][nx] >= 0 && ocean[ny][nx] <= shark_size){
                    // 다음 지역 방문 체크
                    visited[ny][nx] = true;
                    deq.addLast(new int[] {nx, ny, path + 1});
                }
            }
        }

        // 최단 경로 반환
        return new int[] {fish_x, fish_y, minimum_path};
    }

    // 실행함수
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = br.readLine();
        N = Integer.parseInt(line);
        
        // ocean 길이 설정
        ocean = new int[N][N];

        // ocean 입력값 채우기
        StringTokenizer st;
        for(int y = 0; y < N; y++){
            st = new StringTokenizer(br.readLine());
            for(int x = 0; x < N; x++){
                ocean[y][x] = Integer.parseInt(st.nextToken());
            }
        }

        // 아기상어 시작점 찾으면 0으로 바꾸고 아기상어 이동 횟수 구하기
        for(int y = 0; y < N; y++){
            for(int x = 0; x < N; x++){
                // 아기상어의 시작점을 찾았으면
                if(ocean[y][x] == 9){
                    // 시작점 0으로 만들기
                    ocean[y][x] = 0;
                    // 아기상어 최단 시간 구하기
                    System.out.println(baby_shark_move(x, y, 2, 0));
                    break;
                }
            }
        }
    }
}
