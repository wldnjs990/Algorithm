// 현재 행 n줄 만큼 열의 0 ~ n 까지가 전부 n이고 뒤는 순서대로 숫자가 나열됨
// 5x5 2차원 배열을 예시로 들면
// 0번째 줄 12345  0 ~ 0 까지 1(0 + 1)이고 뒤는 순서대로 숫자 나열
// 1번째 줄 22345  0 ~ 1 까지 2(1 + 1)이고 뒤는 순서대로 숫자 나열
// 2번째 줄 33345  0 ~ 2 까지 3(2 + 1)이고 뒤는 순서대로 숫자 나열
// 3번째 줄 44445  0 ~ 3 까지 4(3 + 1)이고 뒤는 순서대로 숫자 나열
// 4번째 줄 55555  0 ~ 4 까지 5(4 + 1)이고 뒤는 순서대로 숫자 나열

// left ~ right 만큼 반복문을 돌려 현재 숫자가 nxn 배열에서 몇 행 몇 열인지 구한다
// 열이 행보다 작으면 행 + 1, 행이 열보다 작으면 열 + 1로 계산한 값을 배열에 담아 반환하면 끝
function solution(n, left, right) {
    const result = []
    for(let i = left; i <= right; i++){
        const row = Math.floor(i / n)
        const col = i % n
        let now;
        if(row >= col) now = row + 1
        else now = col + 1
        result.push(now)
    }
    return result
    
}