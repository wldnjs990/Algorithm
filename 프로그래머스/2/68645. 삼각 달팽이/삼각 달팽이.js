// 삼각형을 2차원 배열로 표현(구역은 전부 0으로 설정)
// DFS나 BFS를 실행해 삼각형을 그린 후에 filter같은 함수를 돌려서 0을 제외한 숫자들을 차례대로 담으면 완성?
function solution(n) {
    // 삼각형 마지막 숫자 구하기
    let finish = 0
    for(let i = 1; i <= n; i++){
        finish += i
    }
    
    // 삼각형 그릴 2차원 배열 만들기
    const arr = []
    for(let i = 0; i < n; i++){
        arr.push(new Array(n).fill(0))
    }
    
    // 이동좌표 만들기(아래, 오른쪽, 좌측 대각선), 현재 방향
    const dx = [0, 1, -1]
    const dy = [1, 0, -1]
    let dir = 0
    
    // 현재 좌표
    let x = 0
    let y = 0
    
    // 시작점 찍기
    arr[0][0] = 1
    
    // 삼각형 만들때 까지 반복하는 반복문
    let count = 1
    while(count < finish){
        count += 1
        let nextX = x + dx[dir]
        let nextY = y + dy[dir]
        
        if(nextX >= n || nextY >= n || arr[nextY][nextX] !== 0){
            // 현재 방향 재설정
            if(dir < 2) dir += 1
            else dir = 0
            // 새로운 방향으로 좌표 수정
            nextX = x + dx[dir]
            nextY = y + dy[dir]
            // 기록
            arr[nextY][nextX] = count
            x = nextX
            y = nextY
        } else {
            // 기록
            arr[nextY][nextX] = count
            x = nextX
            y = nextY
        }
    }
    const result = []
    for(let i = 0; i < n; i++){
        for(let j = 0; j < n; j++){
            if(arr[i][j] !== 0){
                result.push(arr[i][j])
            }
        }
    }
    return result
}