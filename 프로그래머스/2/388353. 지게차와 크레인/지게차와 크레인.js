// 시간복잡도는 굉장히 널널해서 반복문 필요한 만큼 사용해도 될듯
// 문자열 하나 "A" = 접근 가능한 컨테이너만 뺌
// 문자열 둘 "AA" = 모든 컨테이너를 뺌
// 문자열 하나 = 2차원 배열을 순회하며 현재 위치의 상하좌우를 끝까지 탐색해 한 곳이라도 전부 빈 공간이라면 뺄 수 있으므로 제거한다(단, 따로 좌표를 표시해두고 한번에 제거하는 등의 방식을 사용해야 배열을 순회하면서 오류가 발생하지 않을거 같음)
// 문자열 둘 = 배열에 존재하는 모든 문자 제거
// 키 포인트 = 문자열 둘로 모든 요소를 제거하면 빈 공간이 생기는데 컨테이너 사이에 빈 공간이 생기면 현재 위치 상하좌우를 체크할때 빈 공간으로 판단돼서 뺄 수 없는데도 빼지는 상황이 발생할 수 있음
// 해결방안 고민 => 상하좌우를 검사할때 상하좌우별로 끝까지 탐색해 전부다 빈 공간일 경우를 뺄 수 있는 컨테이너로 판단하자
function solution(storage, requests) {
    // storage 문자열 배열로 변환
    storage = storage.map((e)=>{
        return e.split('')
    })
    // 사분면
    const dx = [1, 0, -1, 0]
    const dy = [0, -1, 0, 1]
    // 끝까지 탐색하는 DFS 함수
    function DFS(x, y, dir, blank){
        x += dx[dir]
        y += dy[dir]
        if(y < storage.length && x < storage[0].length && x >= 0 && y >= 0){
            // 현재 위치가 탐색 가능한 위치인가
            if(blank[y][x]){
                // 현재 위치 탐색 완료로 전환
                blank[y][x] = false
                // 현재 이동한 좌표가 빈 공간인지 확인
                if(storage[y][x] === ''){
                    for(let i = 0; i < 4; i++){
                        if(DFS(x, y, i, blank)) return true
                    }
                }
            }
        }else{
            return true
        }
        return false
    }
    for(let request of requests){
        if(request.length === 1){
            // 지게차
            for(let i = 0; i < storage.length; i++){
                for(let j = 0; j < storage[i].length; j++){
                    if(storage[i][j] === request){
                        // 사분면 중 하나라도 접근 가능한지 판단
                        let isEmpty = false
                        for(let k = 0; k < 4; k++){
                            // 이동 지역 표시 지도
                            // 하나씩 진행하려면 지도를 반복문 마다 하나씩 만들어야 할 거 같음
                            // 2차원 배열이라 ... 얕은복사로 참조주소를 바꿀수 없을거 같음
                            // 시간복잡도 모르것다 그냥
                            const blank = new Array(storage.length).fill('').map(e=>{
                                return new Array(storage[0].length).fill(true)
                            })
                            if(DFS(j, i, k, blank)) {
                                isEmpty = true
                            }
                        }
                        // 하나라도 비었다면 출고대기(한번에 다 빼야 오류가 발생 안할듯)
                        if(isEmpty) storage[i][j] = '.'
                    }
                }
            }
            storage = storage.map(e=>{
                return e.map(i=>{
                    if(i === '.') return ''
                    return i
                })
            })
        } else {
            // 크레인
            storage = storage.map(e=>{
                return e.map(i=>{
                    if(i === request[0]) return ''
                    return i
                })
            })
        }
    }
    // 지게차 돌리고 남은 컨테이너 수 출력
    let result = 0
    for(let i = 0; i < storage.length; i++){
        for(let j = 0; j < storage[i].length; j++){
            if(storage[i][j] !== '') result += 1
        }
    }
    return result
    
}