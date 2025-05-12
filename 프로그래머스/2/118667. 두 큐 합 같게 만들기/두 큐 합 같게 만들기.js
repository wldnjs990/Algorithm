// 길이가 같은 두 개의 큐 지급
// 하나의 큐엔 pop, 하나의 큐엔 insert 작업으로 각 큐의 원소값이 같아져야함
// pop, insert 세트를 한번으로 취급
// 두 큐의 합이 같을때 까지의 작업 수행 최솟값 구하기
// 큐 = FIFO

// 두 배열을 통으로 합친 값을 2로 나누면 같은 합의 값(기준값)이 나옴(홀수면 바로 -1 출력)
// queue1의 합과 queue2의 합을 기준값과 비교하며 더 큰 쪽을 shift, 더 작은쪽에 push 해보자
// 근데 이러면 최솟값이 구해질까?

// 여기까지 내 생각

// 답은 구해지는데 시간복잡도에서 문제가 발생
// shift가 O(n)의 시간복잡도를 가져서 큐의 길이가 최대 600,000 * 300,000이 되는거 같은데?
// shift를 사용하지 않고 각 큐의 index를 만들어서 shift 대신 인덱스를 한 칸 앞으로 밀고 push로 배열을 연결하는 방식으로 풀면 됨(풀이봤음)

// 추가로 이 공식의 반복문 최댓값은 두 큐의 길이의 곱연산이라고 한다.

function solution(queue1, queue2) {
    let q1 = queue1.reduce((acc, cur)=> acc + cur, 0)
    let q2 = queue2.reduce((acc, cur)=> acc + cur, 0)
    // 총 합이 홀수면 -1 반환
    if((q1 + q2) % 2 > 0) return -1
    // 기준값 생성
    const baseLine = (q1 + q2) / 2
    // 반복문 종료점
    let endOf = 1000000
    // 큐들의 현재 인덱스
    let q1Idx = 0
    let q2Idx = 0
    // 결과값
    let count = 0
    while(endOf--){
        if(q1 > baseLine){
            let shift = queue1[q1Idx]
            queue2.push(shift)
            q1 -= shift
            q2 += shift
            q1Idx += 1
            count += 1
        } else if(q2 > baseLine){
            let shift = queue2[q2Idx]
            queue1.push(shift)
            q1 += shift
            q2 -= shift
            q2Idx += 1
            count += 1
        } else {
            break;
        }
    }
    // 반복문동안 답이 안나왔다면 -1 출력
    if(endOf <= 0) return -1
    return count
}